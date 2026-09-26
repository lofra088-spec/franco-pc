import { providerSettings, checkOrigin, localVoiceUrl } from '../../../lib/provider-server';

export async function POST(req: Request, context: {params: Promise<{action: string}>}) {
  try {
    checkOrigin(req);
    const {action} = await context.params;
    if (!['tts', 'transcribe', 'speakers'].includes(action)) return new Response(null, {status: 404});
    const settings = await providerSettings();
    const base = localVoiceUrl(settings.xttsUrl);
    let body: BodyInit;
    const headers: Record<string, string> = {};
    if (action === 'tts') {
      const {text} = await req.json();
      if (typeof text !== 'string' || !text.trim() || text.length > 12000) throw new Error('Testo vocale non valido (massimo 12000 caratteri).');
      headers['Content-Type'] = 'application/json';
      body = JSON.stringify({text, speaker: settings.xttsSpeaker || '', language: settings.voiceLanguage || 'it'});
    } else {
      const form = await req.formData();
      const file = form.get('file');
      if (!(file instanceof File) || file.size > 25 * 1024 * 1024) throw new Error('File mancante o superiore a 25 MB.');
      if (action === 'transcribe') form.set('language', settings.voiceLanguage || 'it');
      body = form;
    }
    const response = await fetch(`${base}/${action}`, {method: 'POST', headers, body, signal: AbortSignal.any([req.signal, AbortSignal.timeout(240000)])});
    if (!response.ok) {
      const detail = await response.text();
      return Response.json({error: `Servizio vocale (${response.status}): ${detail.slice(0, 400)}`}, {status: 502});
    }
    return new Response(response.body, {headers: {'Content-Type': response.headers.get('content-type') || 'application/json', 'Cache-Control': 'no-store'}});
  } catch (error) {
    return Response.json({error: `XTTS locale: ${error instanceof Error ? error.message : 'errore'}. Verifica che il servizio vocale sia avviato.`}, {status: 503});
  }
}
