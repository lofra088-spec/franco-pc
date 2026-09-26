'use client';
import {useEffect, useRef, useState} from 'react';
import type {JarvisSettings} from './SettingsModal';
import type {JarvisFunction} from '../lib/functions';

type Message = {role: string; content: string | null; tool_calls?: {id: string; type: 'function'; function: {name: string; arguments: string}}[]; tool_call_id?: string};

export function OpenRouterChat({settings, functions, active, muted}: {settings: JarvisSettings; functions: JarvisFunction[]; active: boolean; muted: boolean}) {
  const [input, setInput] = useState('');
  const [lines, setLines] = useState<{role: string; text: string}[]>([]);
  const [busy, setBusy] = useState(false);
  const [recording, setRecording] = useState(false);
  const [error, setError] = useState('');
  const history = useRef<Message[]>([]);
  const controller = useRef<AbortController | null>(null);
  const recorder = useRef<MediaRecorder | null>(null);
  const stream = useRef<MediaStream | null>(null);
  const audio = useRef<HTMLAudioElement | null>(null);
  const audioUrl = useRef('');
  const generation = useRef(0);
  const locked = useRef(false);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);

  function stopAudio() {
    audio.current?.pause(); audio.current = null;
    if (audioUrl.current) URL.revokeObjectURL(audioUrl.current);
    audioUrl.current = '';
    window.speechSynthesis?.cancel();
  }
  function cancel() {
    generation.current++;
    controller.current?.abort();
    if (recorder.current?.state === 'recording') recorder.current.stop();
    stream.current?.getTracks().forEach(t => t.stop());
    if (timer.current) clearTimeout(timer.current);
    stopAudio(); locked.current = false; setBusy(false); setRecording(false);
  }
  useEffect(() => { if (!active) { cancel(); history.current = []; } return cancel; }, [active]); // eslint-disable-line react-hooks/exhaustive-deps
  useEffect(() => { if (muted) cancel(); }, [muted]); // eslint-disable-line react-hooks/exhaustive-deps

  async function speak(text: string, signal: AbortSignal) {
    stopAudio();
    if (muted || settings.ttsProvider === 'off') return;
    if (settings.ttsProvider !== 'xtts') {
      const utterance = new SpeechSynthesisUtterance(text); utterance.lang = settings.voiceLanguage || 'it';
      window.speechSynthesis?.speak(utterance); return;
    }
    const response = await fetch('/api/voice/tts', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({text}), signal});
    if (!response.ok) throw new Error((await response.json()).error);
    const blob = await response.blob();
    signal.throwIfAborted();
    audioUrl.current = URL.createObjectURL(blob);
    audio.current = new Audio(audioUrl.current);
    audio.current.onended = stopAudio;
    await audio.current.play();
  }

  async function send(text: string) {
    if (!text.trim() || locked.current || !active) return;
    locked.current = true; setBusy(true); setError(''); setInput(''); stopAudio();
    const run = generation.current;
    const abort = new AbortController(); controller.current = abort;
    const next: Message[] = [...history.current, {role: 'user', content: text}];
    setLines(prev => [...prev, {role: 'Tu', text}]);
    // These legacy abilities call OpenAI-specific image/computer-use endpoints.
    // Do not advertise them in OpenRouter mode, so this mode never silently
    // falls back to an OpenAI key.
    const openAiOnly = new Set(['computer_use', 'xray', 'image_generation', '3d_printing']);
    const enabled = functions.filter(fn => settings.enabledFunctions.includes(fn.name) && !openAiOnly.has(fn.name));
    try {
      for (let round = 0; round < 8; round++) {
        const response = await fetch('/api/chat', {method: 'POST', headers: {'Content-Type': 'application/json'}, signal: abort.signal,
          body: JSON.stringify({messages: next, tools: enabled.map(fn => ({type: 'function', function: {name: fn.name, description: fn.tool.description, parameters: fn.tool.parameters}}))})});
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || 'Errore OpenRouter');
        abort.signal.throwIfAborted();
        const message: Message = data.message; next.push(message);
        if (message.tool_calls?.length) {
          for (const call of message.tool_calls) {
            abort.signal.throwIfAborted();
            const fn = enabled.find(f => f.name === call.function.name);
            let result: unknown;
            try { result = fn ? await fn.handler(JSON.parse(call.function.arguments)) : {error: 'Funzione non abilitata'}; }
            catch (e) { result = {error: String(e)}; }
            next.push({role: 'tool', tool_call_id: call.id, content: JSON.stringify(result ?? null)});
          }
          continue;
        }
        history.current = next;
        const reply = message.content || 'Nessuna risposta testuale.';
        setLines(prev => [...prev, {role: 'Jarvis', text: reply}]);
        await speak(reply, abort.signal); return;
      }
      throw new Error('Limite di 8 passaggi raggiunto. Riprova con una richiesta più breve.');
    } catch (e) { if (!abort.signal.aborted) setError(e instanceof Error ? e.message : String(e)); }
    finally { if (run === generation.current) {locked.current = false; setBusy(false);} }
  }

  async function record() {
    if (recording) {recorder.current?.stop(); return;}
    if (busy || muted || !active) return;
    const run = generation.current; setError(''); stopAudio();
    try {
      const media = await navigator.mediaDevices.getUserMedia({audio: true});
      if (run !== generation.current) {media.getTracks().forEach(t => t.stop()); return;}
      stream.current = media;
      const chunks: Blob[] = [];
      const rec = new MediaRecorder(media); recorder.current = rec;
      rec.ondataavailable = event => {if (event.data.size) chunks.push(event.data);};
      rec.onstop = async () => {
        media.getTracks().forEach(t => t.stop()); if (timer.current) clearTimeout(timer.current); setRecording(false);
        if (run !== generation.current) return;
        const abort = new AbortController(); controller.current = abort;
        locked.current = true; setBusy(true);
        try {
          const form = new FormData(); form.append('file', new Blob(chunks, {type: rec.mimeType}), 'recording.webm');
          const res = await fetch('/api/voice/transcribe', {method: 'POST', body: form, signal: abort.signal});
          const data = await res.json(); if (!res.ok) throw new Error(data.error);
          if (run !== generation.current) return;
          locked.current = false; setBusy(false);
          if (data.text?.trim()) await send(data.text); else setError('Non ho rilevato parole. Riprova.');
        } catch (e) {if (!abort.signal.aborted) setError(String(e));}
        finally {if (run === generation.current) {locked.current = false; setBusy(false);}}
      };
      rec.start(); setRecording(true); timer.current = setTimeout(() => {if (rec.state === 'recording') rec.stop();}, 60000);
    } catch (e) {setError(`Microfono: ${String(e)}`);}
  }

  return <section className="fixed bottom-4 left-1/2 -translate-x-1/2 z-[60] w-[min(680px,94vw)] rounded-xl border border-cyan-700 bg-black/95 p-3 text-sm text-cyan-100 pointer-events-auto">
    <div className="max-h-48 overflow-y-auto space-y-2" aria-live="polite">{lines.slice(-30).map((line, i) => <p key={i} className="whitespace-pre-wrap"><b>{line.role}:</b> {line.text}</p>)}</div>
    {error && <p role="alert" className="text-red-300 my-2">{error}</p>}
    <form className="flex gap-2 mt-2" onSubmit={e => {e.preventDefault(); void send(input);}}>
      <input aria-label="Messaggio per Jarvis" className="flex-1 min-w-0 bg-slate-900 rounded p-2" value={input} onChange={e => setInput(e.target.value)} placeholder={active ? 'Scrivi a Jarvis…' : 'Attiva Jarvis per iniziare'} disabled={!active || busy || recording}/>
      <button type="submit" disabled={!active || busy || recording || !input.trim()} className="px-2 disabled:opacity-40">{busy ? 'Attendi…' : 'Invia'}</button>
      <button type="button" onClick={() => void record()} disabled={!active || busy || muted} className="px-2 disabled:opacity-40">{recording ? 'Termina' : 'Microfono'}</button>
      <button type="button" onClick={cancel} aria-label="Interrompi risposta">Stop</button>
    </form>
    <p className="text-xs text-slate-400 mt-1">OpenRouter · Microfono a turni (massimo 60 s) · Voce: {settings.ttsProvider || 'sistema'}</p>
  </section>;
}
