"""Optional voice I/O, loaded on demand; no legacy core or local neural models."""
from __future__ import annotations

import math
import os
import re
import struct
import subprocess
import threading
import time
from collections import deque

from .endpointing import AdaptiveEndpointDetector


def speech_text(text):
    text = re.sub(r"```[\s\S]*?(?:```|$)", " Il codice è nella chat. ", str(text))
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", "il link nella chat", text)
    text = re.sub(r"<[^>]*>|[*_`#]", " ", text)
    return re.sub(r"\s+", " ", text).strip()[:16000]


class DesktopSpeech:
    """SAPI runs in a disposable child, so mute can stop an utterance immediately."""

    _SCRIPT = (
        "[Console]::InputEncoding = New-Object System.Text.UTF8Encoding($false); "
        "$text=[Console]::In.ReadToEnd(); $s=New-Object -ComObject SAPI.SpVoice; "
        "$voices=$s.GetVoices(); foreach($v in $voices){ "
        "if($v.GetAttribute('Language') -match '^410(;|$)'){ $s.Voice=$v; break }}; "
        # Synchronous Speak keeps the COM host alive for the whole utterance;
        # terminating this child is also how the mute button interrupts it.
        "$null=$s.Speak($text,0)"
    )

    def __init__(self):
        self._lock = threading.Lock()
        self._process = None
        self._closed = False

    def say(self, text):
        text = speech_text(text)
        if not text:
            return
        if os.name != "nt":
            raise RuntimeError("La voce Windows è disponibile soltanto su Windows.")
        with self._lock:
            if self._closed:
                return
            process = subprocess.Popen(
                ["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", self._SCRIPT],
                stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
            self._process = process
        try:
            _, _error = process.communicate(text.encode("utf-8"), timeout=180)
            if process.returncode and self._process is process:
                raise RuntimeError("La sintesi vocale di Windows non è disponibile.")
        except subprocess.TimeoutExpired:
            process.kill()
            process.communicate()
            raise RuntimeError("Sintesi vocale interrotta per timeout.") from None
        finally:
            with self._lock:
                if self._process is process:
                    self._process = None

    def stop(self):
        with self._lock:
            process, self._process = self._process, None
        if process and process.poll() is None:
            try:
                process.terminate()
            except OSError:
                pass

    def close(self):
        with self._lock:
            self._closed = True
        self.stop()


class DesktopMicrophone:
    """Continuous 16 kHz capture plus coalesced Italian ASR snapshots.

    Uses sounddevice RawInputStream (no NumPy) and SpeechRecognition's Google
    recognizer. This is incremental snapshot recognition, not token streaming.
    Only one network recognition runs at once. Partial text never triggers actions.
    """

    RATE = 16000
    MAX_AUDIO_SECONDS = 40

    def __init__(self):
        self._cv = threading.Condition()
        self._generation = 0
        self._closed = False
        self._stop = threading.Event()
        self._stop.set()
        self._capture = None
        self._asr = None
        self._pending = None
        self._partial = ""
        self._prefix = ""
        self._on_partial = self._on_final = self._on_status = lambda _: None
        self._detector = AdaptiveEndpointDetector()

    def start(self, on_partial, on_final, on_status):
        # Optional imports happen off the GUI thread, and only when mic is enabled.
        try:
            import sounddevice as sd
            import speech_recognition as sr
        except ImportError as error:
            raise RuntimeError("Microfono non disponibile: installa le dipendenze franco[desktop].") from error
        with self._cv:
            if self._closed:
                return
            if self._capture and self._capture.is_alive():
                if not self._stop.is_set():
                    return
                raise RuntimeError("Il microfono si sta chiudendo. Riprova fra un momento.")
            self._generation += 1
            generation = self._generation
            self._stop = threading.Event()
            self._partial = self._prefix = ""
            self._on_partial, self._on_final, self._on_status = on_partial, on_final, on_status
            if self._asr is None:
                self._asr = threading.Thread(target=self._recognize, args=(sr,), daemon=True, name="FrancoV7-ASR")
                self._asr.start()
            self._capture = threading.Thread(target=self._listen, args=(sd, generation, self._stop),
                                             daemon=True, name="FrancoV7-Microphone")
            self._capture.start()

    def _current(self, generation):
        return not self._closed and generation == self._generation and not self._stop.is_set()

    def _emit(self, generation, callback, value):
        with self._cv:
            if not self._current(generation):
                return
        # Device callbacks may enter the controller and must never run while
        # this adapter's lock is held.
        callback(value)

    def _snapshot(self, generation, turn, audio, final):
        with self._cv:
            # Preserve final snapshots over speculative work; bounded to one.
            if self._current(generation) and (self._pending is None or not self._pending[-1]):
                self._pending = (generation, turn, bytes(audio), final)
                self._cv.notify_all()

    def _listen(self, sd, generation, stop):
        frames = deque(maxlen=32)
        lock = threading.Lock()
        audio = bytearray()
        last_voice = started = last_snapshot = None
        floor = 80.0
        turn = 0
        def capture(raw, count, timing, status):
            with lock:
                frames.append(bytes(raw))
        try:
            with sd.RawInputStream(samplerate=self.RATE, channels=1, dtype="int16", blocksize=1024, callback=capture):
                self._emit(generation, self._on_status, {"status": "listening", "text": "Ascolto attivo · italiano"})
                while not stop.wait(.02):
                    with lock:
                        batch = list(frames)
                        frames.clear()
                    for raw in batch:
                        now = time.monotonic()
                        samples = struct.unpack(f"<{len(raw)//2}h", raw)
                        rms = math.sqrt(sum(value*value for value in samples)/max(1,len(samples)))
                        voiced = rms > max(150, floor * 2.6)
                        if not audio and not voiced:
                            floor = .97*floor + .03*rms
                            continue
                        if not audio:
                            started = last_snapshot = now
                            turn += 1
                            with self._cv:
                                self._partial = ""
                        audio.extend(raw)
                        if voiced:
                            last_voice = now
                        silence = now-(last_voice or now)
                        if now-last_snapshot >= .8 and len(audio) >= self.RATE:
                            self._snapshot(generation, turn, audio, False)
                            last_snapshot = now
                        with self._cv:
                            partial = self._partial
                        decision = self._detector.decide(partial, silence)
                        end = decision.should_finalize if partial else silence >= 1.4
                        if end and now-started >= .25:
                            self._snapshot(generation, turn, audio, True)
                            audio.clear()
                            last_voice = None
                        elif len(audio) >= self.RATE*2*self.MAX_AUDIO_SECONDS:
                            audio.clear()
                            last_voice = None
                            self._emit(generation, self._on_status, {
                                "status": "listening", "text": "Frase troppo lunga: fai una breve pausa e ripeti la richiesta."})
        except Exception:  # noqa: BLE001 - native audio backends vary by host
            self._emit(generation, self._on_status, {
                "status": "error", "text": "Microfono non accessibile. Verifica il dispositivo predefinito e riprova."})

    def _recognize(self, sr):
        recognizer = sr.Recognizer()
        recognizer.operation_timeout = 7
        last_turn = None
        while True:
            with self._cv:
                self._cv.wait_for(lambda: self._closed or self._pending is not None)
                if self._closed:
                    return
                generation, turn, audio, final = self._pending
                self._pending = None
            try:
                text = recognizer.recognize_google(sr.AudioData(audio, self.RATE, 2), language="it-IT").strip()
                with self._cv:
                    if not self._current(generation):
                        continue
                    if last_turn == (generation, turn) and not final:
                        continue
                    combined = (self._prefix + " " + text).strip()[:4000]
                    self._partial = combined
                self._emit(generation, self._on_partial, combined)
                if final:
                    last_turn = (generation, turn)
                    if self._detector._looks_truncated(combined):
                        with self._cv:
                            self._prefix = combined
                        self._emit(generation, self._on_status, {
                            "status": "listening", "text": "La frase sembra incompleta: continua, ti ascolto."})
                    else:
                        with self._cv:
                            self._prefix = ""
                        self._emit(generation, self._on_final, combined)
            except sr.UnknownValueError:
                if final:
                    self._emit(generation, self._on_status, {"status":"listening", "text":"Non ho capito la frase, puoi ripeterla."})
            except Exception:  # noqa: BLE001 - remote recognizer boundary
                if final:
                    self._emit(generation, self._on_status, {"status":"error", "text":"Trascrizione non raggiungibile. Puoi continuare dalla chat."})

    def stop(self):
        with self._cv:
            self._generation += 1
            self._stop.set()
            self._pending = None
            self._prefix = self._partial = ""
            self._cv.notify_all()

    def close(self):
        with self._cv:
            self._closed = True
        self.stop()
