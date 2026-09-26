"""Local XTTS lifecycle and speech telemetry, independent of the application core."""
from __future__ import annotations

from array import array
import html
import io
import json
import math
import os
from pathlib import Path
import re
import subprocess
import threading
import time
import urllib.error
import urllib.request
import uuid
import wave


def spoken_text(text: str) -> str:
    """Prepare natural Italian speech without reading display-only markup.

    Punctuation still controls prosody. Literal words such as ``virgola`` are
    preserved because they may be the subject of the user's question.
    """
    text = html.unescape(str(text or ""))
    text = re.sub(r"<(think|analysis|script|style)\b[^>]*>[\s\S]*?</\1\s*>", " ", text, flags=re.I)
    text = re.sub(r"(`{3,}|~{3,})[^\n]*\n[\s\S]*?(?:\1|$)", " Il codice è nella chat. ", text)
    text = re.sub(r"```[\s\S]*?(?:```|$)", " Il codice è nella chat. ", text)
    text = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"(?:https?://|www\.)[^\s<>]+", "il link nella chat", text)
    text = re.sub(r"(?m)^\s*\|?\s*:?-{3,}.*$", " ", text)
    text = re.sub(r"(?m)^\s*(?:#{1,6}\s+|[>]+\s*|[-*+•]\s+(?:\[[ xX]\]\s*)?|\d+[.)]\s+)", "", text)
    text = re.sub(r"<br\s*/?>|</(?:p|div|li|h[1-6])\s*>", ". ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"(?<=\w)_(?=\w)", " ", text)
    text = re.sub(r"[*_`~]", "", text)
    text = re.sub(r"\s*\|\s*", ", ", text)
    text = re.sub(r"\b([01]?\d|2[0-3]):([0-5]\d)\b", r"\1 e \2", text)
    text = text.replace(":", ",").replace(";", ",").replace("…", ".")
    text = re.sub(r"[\U0001F000-\U0001FAFF\u2600-\u27BF\ufe0f\u200d]", " ", text)
    text = re.sub(r"[.!?]{2,}", ".", text)
    text = re.sub(r"(?:[,;]\s*){2,}", ", ", text)
    text = re.sub(r"\s+([,.!?])", r"\1", text)
    return re.sub(r"\s+", " ", text).strip(" ,\n\t")


def wav_envelope(audio: bytes, step_ms: int = 40) -> list[float]:
    """RMS from the generated PCM, indexed using the actual playback clock."""
    try:
        with wave.open(io.BytesIO(audio), "rb") as wav:
            if wav.getsampwidth() != 2:
                return []
            rate, channels = wav.getframerate(), wav.getnchannels()
            samples = array("h", wav.readframes(wav.getnframes()))
        step = max(1, int(rate * channels * step_ms / 1000))
        return [min(1.0, math.sqrt(sum(v * v for v in samples[i:i + step]) /
                                 len(samples[i:i + step])) / 7000)
                for i in range(0, len(samples), step)]
    except (ValueError, EOFError, wave.Error):
        return []


class PermanentXTTSFailure(RuntimeError):
    """A configuration/model error requiring an explicit retry after repair."""


class XTTSService:
    """One local server shared by FRANCO instances, with visible failure states."""
    _launch_lock = threading.Lock()

    def __init__(self, state, logger):
        self.state, self.logger = state, logger
        # orb_voice.py lives in <project>/src/franco/.  Keep generated files
        # and the embedded XTTS runtime anchored to the real project root.
        self.project = Path(__file__).resolve().parents[2]
        self.franco_root = Path(os.environ.get("FRANCO_ROOT", str(Path(__file__).resolve().parents[4])))
        self.url = "http://127.0.0.1:8790"
        self.process = None
        self._supervisor_stop = threading.Event()
        self._supervisor_thread = None
        self._permanent_error = ""
        self._request_lock = threading.Lock()
        self._last_health = None

    def health(self):
        try:
            with urllib.request.urlopen(self.url + "/health", timeout=1) as response:
                payload = response.read(16000)
        except urllib.error.HTTPError as error:
            if error.code == 503:
                payload = error.read(16000)
            else:
                raise PermanentXTTSFailure(f"Porta XTTS occupata: HTTP {error.code}") from error
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            return None
        try:
            status = json.loads(payload)
        except (ValueError, UnicodeDecodeError) as error:
            raise PermanentXTTSFailure("La porta 8790 non risponde come un server XTTS.") from error
        if not isinstance(status, dict) or status.get("engine") != "xtts" or not isinstance(status.get("ready"), bool):
            raise PermanentXTTSFailure("La porta 8790 è occupata da un altro servizio.")
        self._last_health = status
        return status

    def reset_error(self):
        """Allow retry after the user repairs a model/runtime configuration."""
        self._permanent_error = ""
        self.state.set("tts_error", "", notify=False)

    def _ready(self, status):
        self._permanent_error = ""
        self.state.set("tts_status", "ready", notify=False)
        self.state.set("tts_error", "", notify=False)
        if status.get("pid"):
            self.state.set("xtts_pid", status["pid"], notify=False)

    def ensure_ready(self, cancel: threading.Event, timeout=150):
        if cancel.is_set():
            raise InterruptedError("Sintesi interrotta")
        deadline = time.monotonic() + timeout
        with self._launch_lock:
            status = self.health()
            if status and status.get("ready"):
                self._ready(status)
                return
            if status and status.get("error"):
                self._permanent_error = str(status["error"])
            if self._permanent_error:
                raise PermanentXTTSFailure(self._permanent_error)
            if status is None and (self.process is None or self.process.poll() is not None):
                configured = os.environ.get("FRANCO_XTTS_PYTHON", "").strip()
                candidates = [
                    Path(configured) if configured else None,
                    Path(r"E:\Nuova cartella\Jarvis\resources\jarvis-voice\.venv\Scripts\python.exe"),
                    self.project / ".runtime" / "xtts-python" / "python.exe",
                    self.franco_root / "xtts_env" / "Scripts" / "python.exe",
                ]
                python = next((candidate for candidate in candidates if candidate and candidate.is_file()), None)
                if python is None:
                    self._permanent_error = "Interprete XTTS mancante. Imposta FRANCO_XTTS_PYTHON."
                    raise PermanentXTTSFailure(self._permanent_error)
                logdir = self.project / "franco_output" / "logs"
                logdir.mkdir(parents=True, exist_ok=True)
                env = os.environ.copy()
                numba_cache = self.project / ".runtime" / "numba-cache"
                numba_cache.mkdir(parents=True, exist_ok=True)
                env.update(OMP_NUM_THREADS="1", MKL_NUM_THREADS="1",
                           FRANCO_ROOT=str(self.franco_root), PYTHONUNBUFFERED="1",
                           NUMBA_CACHE_DIR=str(numba_cache), NUMBA_DISABLE_CACHING="1")
                try:
                    with (logdir / "xtts-server.log").open("ab") as log:
                        self.process = subprocess.Popen(
                            [str(python), str(Path(__file__).with_name("xtts_server.py"))],
                            cwd=str(self.project), env=env, stdout=log, stderr=log,
                            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
                        self.state.set("xtts_pid", self.process.pid, notify=False)
                except OSError as error:
                    self._permanent_error = "Impossibile avviare XTTS: " + str(error)
                    raise PermanentXTTSFailure(self._permanent_error) from error
        while not cancel.is_set():
            status = self.health()
            if status and status.get("ready"):
                self._ready(status)
                return
            if status and status.get("error"):
                self._permanent_error = str(status["error"])
                raise PermanentXTTSFailure(self._permanent_error)
            if self.process is not None and self.process.poll() is not None:
                raise RuntimeError("XTTS si è chiuso. Dettagli in franco_output/logs/xtts-server.log.")
            if time.monotonic() >= deadline:
                raise RuntimeError("XTTS sta impiegando troppo tempo. Controlla il registro della voce.")
            self.state.set("tts_status", "loading")
            cancel.wait(0.35)
        raise InterruptedError("Sintesi interrotta")

    def start_supervisor(self):
        """Keep the local voice server alive for the lifetime of FRANCO."""
        if self._supervisor_thread and self._supervisor_thread.is_alive():
            return
        self._supervisor_stop.clear()
        self._supervisor_thread = threading.Thread(
            target=self._supervise, daemon=True, name="XTTS-Supervisor")
        self._supervisor_thread.start()

    def _supervise(self):
        retry_delay = 2.0
        consecutive_failures = 0
        while not self._supervisor_stop.is_set():
            try:
                if self.state.get("speech_muted", False):
                    self.state.set("tts_status", "sleeping", notify=False)
                    # The server is shared. Muting one window must never kill
                    # another window's speech or repeatedly reload the model.
                    self._supervisor_stop.wait(3.0)
                    continue
                status = self.health()
                if status and status.get("ready"):
                    if not self._request_lock.locked():
                        self._ready(status)
                    retry_delay = 2.0
                    consecutive_failures = 0
                    self._supervisor_stop.wait(5.0)
                    continue
                if self._permanent_error:
                    self._supervisor_stop.wait(10.0)
                    continue
                self.state.set("tts_status", "restarting", notify=False)
                self.ensure_ready(self._supervisor_stop, timeout=180)
                retry_delay = 2.0
                consecutive_failures = 0
            except InterruptedError:
                break
            except Exception as error:
                consecutive_failures += 1
                if isinstance(error, PermanentXTTSFailure) or consecutive_failures >= 3:
                    self._permanent_error = str(error)
                self.state.set("tts_status", "error", notify=False)
                self.state.set("tts_error", str(error), notify=False)
                self.logger.warning("TTS", f"XTTS non disponibile: {error}")
                if self.process is not None and self.process.poll() is not None:
                    self.process = None
                self._supervisor_stop.wait(retry_delay)
                retry_delay = min(30.0, retry_delay * 1.7)

    def stop_supervisor(self):
        """Stop monitoring; the shared server remains available to other clients."""
        self._supervisor_stop.set()
        thread = self._supervisor_thread
        if thread and thread.is_alive() and thread is not threading.current_thread():
            thread.join(timeout=2.0)

    def _cancel_request(self, request_id):
        if not (self._last_health or {}).get("supports_cancel"):
            return
        try:
            request = urllib.request.Request(self.url + "/cancel", data=json.dumps({
                "request_id": request_id,
            }).encode("utf-8"), headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(request, timeout=2) as response:
                response.read(2000)
        except (OSError, ValueError):
            pass

    def synthesize(self, text: str, cancel: threading.Event) -> bytes:
        prepared = spoken_text(text)
        if not prepared or not re.search(r"\w", prepared):
            raise ValueError("Il messaggio non contiene testo da pronunciare.")
        if len(prepared) > 6000:
            raise ValueError("Dividi il messaggio vocale in parti da massimo 6000 caratteri.")
        self.ensure_ready(cancel)
        if cancel.is_set():
            raise InterruptedError("Sintesi interrotta")
        if not self._request_lock.acquire(blocking=False):
            raise RuntimeError("XTTS sta terminando la frase precedente. Riprova tra un momento.")
        self.state.set("tts_status", "synthesizing")
        request_id = uuid.uuid4().hex
        request = urllib.request.Request(self.url + "/tts", data=json.dumps({
            "text": prepared, "language": "it", "request_id": request_id,
            "speaker": os.environ.get("FRANCO_XTTS_SPEAKER", "Ludvig Milivoj"),
        }).encode("utf-8"), headers={"Content-Type": "application/json"})
        done, result = threading.Event(), {}

        def request_audio():
            try:
                with urllib.request.urlopen(request, timeout=180) as response:
                    audio = response.read(24 * 1024 * 1024 + 1)
                    if len(audio) > 24 * 1024 * 1024:
                        raise RuntimeError("Il messaggio vocale supera il limite audio.")
                    result["audio"] = audio
            except urllib.error.HTTPError as error:
                detail = error.read(2000).decode("utf-8", errors="replace")
                try:
                    detail = json.loads(detail).get("error", detail)
                except (ValueError, AttributeError):
                    pass
                result["error"] = RuntimeError(f"Sintesi XTTS: {detail}")
            except Exception as error:
                result["error"] = error
            finally:
                self._request_lock.release()
                done.set()

        # Only one worker may outlive a cancelled call. Holding the lock until
        # it exits prevents unbounded abandoned threads or queued GPU jobs.
        threading.Thread(target=request_audio, daemon=True, name="XTTS-request").start()
        deadline = time.monotonic() + 180
        while not done.wait(0.08):
            if cancel.is_set() or self._supervisor_stop.is_set() or time.monotonic() >= deadline:
                threading.Thread(target=self._cancel_request, args=(request_id,),
                                 daemon=True, name="XTTS-cancel").start()
                if cancel.is_set() or self._supervisor_stop.is_set():
                    self.state.set("tts_status", "interrupted", notify=False)
                    raise InterruptedError("Sintesi interrotta")
                raise TimeoutError("XTTS non ha terminato il messaggio entro tre minuti.")
        if cancel.is_set() or self._supervisor_stop.is_set():
            raise InterruptedError("Sintesi interrotta")
        if "error" in result:
            raise result["error"]
        audio = result["audio"]
        if audio[:4] != b"RIFF" or audio[8:12] != b"WAVE":
            raise RuntimeError("XTTS ha restituito un audio non valido.")
        try:
            with wave.open(io.BytesIO(audio), "rb") as wav:
                if wav.getsampwidth() != 2 or wav.getnchannels() != 1 or wav.getnframes() == 0:
                    raise ValueError("Formato audio vocale non supportato")
                if len(wav.readframes(wav.getnframes())) != wav.getnframes() * 2:
                    raise ValueError("Audio vocale incompleto")
        except (EOFError, wave.Error, ValueError) as error:
            raise RuntimeError("XTTS ha restituito un audio incompleto o non valido.") from error
        self.state.set("tts_status", "ready", notify=False)
        return audio
