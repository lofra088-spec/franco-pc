"""Persistent XTTS worker. Runs in its own Python environment on loopback only."""
from __future__ import annotations

import io
import json
import os
from pathlib import Path
import re
import socket
import threading
import time
import uuid
import wave
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
ROOT = Path(os.environ.get("FRANCO_ROOT", str(Path(__file__).resolve().parents[4])))
MODEL = ROOT / "models" / "tts_cache" / "tts" / "tts_models--multilingual--multi-dataset--xtts_v2"
os.environ.setdefault("TTS_HOME", str(ROOT / "models" / "tts_cache"))
model = None
error = None
generation_lock = threading.Lock()
request_lock = threading.Lock()
active_requests = {}
cancelled_requests = {}
started_at = time.monotonic()


def load_model():
    global model, error
    try:
        for filename in ("model.pth", "config.json", "speakers_xtts.pth", "vocab.json"):
            if not (MODEL / filename).is_file():
                raise RuntimeError("File del modello XTTS mancante: " + str(MODEL / filename))
        import torch
        torch.set_num_threads(1)
        from TTS.api import TTS
        # Uses only the user's existing local model; no implicit licence acceptance.
        instance = TTS(
            model_path=str(MODEL),
            config_path=str(MODEL / "config.json"),
            speakers_file_path=str(MODEL / "speakers_xtts.pth"),
            progress_bar=False,
        )
        instance.to("cuda" if torch.cuda.is_available() else "cpu")
        error = None
        model = instance
        print("XTTS pronto", flush=True)
    except Exception as exc:
        error = str(exc)
        import traceback
        traceback.print_exc()


def chunks(text, limit=230):
    result, current = [], ""
    for word in text.split():
        if len(word) > limit:
            raise ValueError("Una parola supera il limite vocale: usa una frase più breve.")
        if current and len(current) + len(word) + 1 > limit:
            result.append(current)
            current = ""
        current += (" " if current else "") + word
        if len(current) > 60 and re.search(r"[.!?]$", current):
            result.append(current)
            current = ""
    if current:
        result.append(current)
    return result


def cancel_request(request_id):
    """Cancel only the matching utterance, including an arriving request race."""
    with request_lock:
        now = time.monotonic()
        for key, expiry in list(cancelled_requests.items()):
            if expiry < now:
                cancelled_requests.pop(key, None)
        while len(cancelled_requests) >= 256:
            cancelled_requests.pop(next(iter(cancelled_requests)))
        cancelled_requests[request_id] = now + 240
        active = active_requests.get(request_id)
        if active is not None:
            active.set()
        return active is not None


class XTTSHTTPServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False
    allow_reuse_address = False

    def server_bind(self):
        # Windows SO_REUSEADDR permits two binds; exclusive ownership protects
        # the single model instance even when two FRANCO clients launch at once.
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


class Handler(BaseHTTPRequestHandler):
    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def log_message(self, *args):
        pass

    def reply(self, status, body, content_type="application/json"):
        if not isinstance(body, bytes):
            body = json.dumps(body, ensure_ascii=False).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, TimeoutError, OSError):
            pass
        self.close_connection = True

    def local_request(self):
        allowed_hosts = {"127.0.0.1", "localhost",
                         f"127.0.0.1:{self.server.server_port}",
                         f"localhost:{self.server.server_port}"}
        if (self.headers.get("Host", "").lower() not in allowed_hosts
                or self.headers.get("Origin")
                or self.headers.get("Sec-Fetch-Site") == "cross-site"):
            self.reply(403, {"error": "Usa il client locale FRANCO"})
            return False
        return True

    def read_json(self, max_length=24000):
        if self.headers.get("Transfer-Encoding"):
            raise ValueError("Usa una richiesta JSON con dimensione esplicita")
        if self.headers.get_content_type() != "application/json":
            raise ValueError("È richiesto un contenuto JSON")
        length = int(self.headers.get("Content-Length", "0"))
        if not 1 <= length <= max_length:
            raise ValueError("Dimensione richiesta non valida")
        raw = self.rfile.read(length)
        if len(raw) != length:
            raise ValueError("Richiesta incompleta")
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("Il contenuto JSON deve essere un oggetto")
        return data

    def do_GET(self):
        if not self.local_request():
            return
        if self.path == "/health":
            self.reply(200 if model is not None else 503,
                       {"ready": model is not None, "error": error, "engine": "xtts",
                        "pid": os.getpid(), "busy": generation_lock.locked(),
                        "permanent_error": bool(error), "protocol": 2,
                        "supports_cancel": True,
                        "uptime_seconds": round(time.monotonic() - started_at, 1)})
        elif self.path == "/speakers":
            self.reply(200, {"speakers": list(model.speakers or []) if model else []})
        else:
            self.reply(404, {"error": "Endpoint inesistente"})

    def do_POST(self):
        if not self.local_request():
            return
        if self.path == "/cancel":
            try:
                data = self.read_json(1000)
                request_id = data.get("request_id", "")
                if not isinstance(request_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{8,64}", request_id):
                    raise ValueError("Identificatore vocale non valido")
                active = cancel_request(request_id)
                self.reply(200, {"cancelled": True, "active": active})
            except (ValueError, TypeError, UnicodeDecodeError, TimeoutError) as exc:
                self.reply(400, {"error": str(exc)})
            return
        if self.path != "/tts":
            self.reply(404, {"error": "Endpoint inesistente"})
            return
        if model is None:
            self.reply(503, {"error": error or "Modello in caricamento"})
            return
        try:
            data = self.read_json()
            text = data.get("text", "")
            if not isinstance(text, str) or not text.strip() or len(text) > 6000:
                raise ValueError("Il testo deve contenere da 1 a 6000 caratteri")
            speaker = data.get("speaker", "Ludvig Milivoj")
            language = data.get("language", "it")
            if not isinstance(speaker, str) or speaker not in (model.speakers or []):
                raise ValueError("Voce XTTS non disponibile: " + str(speaker))
            if not isinstance(language, str) or language not in (model.languages or []):
                raise ValueError("Lingua XTTS non disponibile")
            request_id = data.get("request_id", uuid.uuid4().hex)
            if not isinstance(request_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{8,64}", request_id):
                raise ValueError("Identificatore vocale non valido")
            parts = chunks(text)
        except (ValueError, TypeError, AttributeError, UnicodeDecodeError, TimeoutError) as exc:
            self.reply(400, {"error": str(exc)})
            return
        if not generation_lock.acquire(blocking=False):
            self.reply(429, {"error": "La voce sta già elaborando un'altra frase"})
            return
        cancellation = threading.Event()
        with request_lock:
            active_requests[request_id] = cancellation
            if cancelled_requests.get(request_id, 0) >= time.monotonic():
                cancellation.set()
        audio_parts = []
        try:
            import numpy as np
            import torch
            deadline = time.monotonic() + 175
            rate = int(model.synthesizer.output_sample_rate)
            if not 8000 <= rate <= 96000:
                raise RuntimeError("Frequenza audio XTTS non valida")
            total_samples = 0
            for part in parts:
                if cancellation.is_set():
                    raise InterruptedError("Sintesi interrotta")
                if time.monotonic() >= deadline:
                    raise TimeoutError("La generazione vocale ha superato il tempo disponibile")
                with torch.inference_mode():
                    samples = model.tts(text=part, language=language, speaker=speaker,
                                        split_sentences=False)
                if cancellation.is_set():
                    raise InterruptedError("Sintesi interrotta")
                samples = np.asarray(samples, dtype=np.float32).reshape(-1)
                total_samples += len(samples)
                if total_samples * 2 > 24 * 1024 * 1024:
                    raise ValueError("Il messaggio vocale supera il limite audio")
                audio_parts.append(samples)
            if not total_samples:
                raise RuntimeError("XTTS non ha prodotto campioni audio")
            samples = np.concatenate(audio_parts)
            samples = np.nan_to_num(samples, nan=0, posinf=1, neginf=-1)
            pcm = (np.clip(samples, -1, 1) * 32767).astype("<i2").tobytes()
            out = io.BytesIO()
            with wave.open(out, "wb") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(rate)
                wav.writeframes(pcm)
            self.reply(200, out.getvalue(), "audio/wav")
        except InterruptedError as exc:
            self.reply(409, {"error": str(exc), "cancelled": True})
        except TimeoutError as exc:
            self.reply(504, {"error": str(exc)})
        except Exception as exc:
            self.reply(500, {"error": str(exc)})
        finally:
            audio_parts.clear()
            with request_lock:
                active_requests.pop(request_id, None)
                cancelled_requests.pop(request_id, None)
            generation_lock.release()
            # Torch's allocator reuses its cache for the next utterance.
            # Calling empty_cache after every sentence adds latency; tensors
            # and PCM buffers are released naturally when this handler exits.


def main():
    # Bind before loading: simultaneous launches cannot duplicate the GPU model.
    try:
        server = XTTSHTTPServer(("127.0.0.1", 8790), Handler)
    except OSError as exc:
        print("XTTS non avviato: porta 8790 già occupata o non disponibile. " + str(exc), flush=True)
        return 1
    threading.Thread(target=load_model, daemon=True, name="XTTS-loader").start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        with request_lock:
            for cancellation in active_requests.values():
                cancellation.set()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
