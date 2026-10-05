"""Bounded, Tk-independent coordination for the Franco V7 desktop.

Only the command worker touches the runtime. Device adapters (or zero-argument
adapter factories) are optional and are never constructed on the UI thread.
Their stop/close methods must be thread-safe and cancel their own pending I/O.
Python cannot interrupt an arbitrary adapter or runtime call already in flight;
cancellation suppresses its output and shutdown never waits for it.
"""
from __future__ import annotations

from collections import deque
from threading import Condition, Thread
from typing import Any


class DesktopController:
    MAX_EVENTS = 128
    MAX_TEXT_CHARS = 16_000
    MAX_PARTIAL_CHARS = 4_000
    MAX_STATUS_CHARS = 512

    def __init__(self, runtime, speech=None, microphone=None):
        self.runtime = runtime
        self._cv = Condition()
        self._events: deque[dict[str, Any]] = deque(maxlen=self.MAX_EVENTS)
        self._closed = False
        self._busy = False
        self._running = False
        self._microphone_enabled = False
        self._voice_enabled = True
        self._status = "Pronto"
        self._turn = 0
        self._mic_revision = 0
        self._voice_revision = 0
        self._pending: tuple[int, str] | None = None
        self._partial: tuple[int, str] | None = None
        self._utterance: tuple[int, int, str] | None = None
        self._sources = {"speech": speech, "microphone": microphone}
        self._devices: dict[str, Any] = {}
        self._threads: dict[str, Thread] = {}
        self._finished: set[str] = set()
        self._stop_requested = {"speech": 0, "microphone": 0}
        self._stop_done = {"speech": 0, "microphone": 0}
        self._device_closed: set[str] = set()
        with self._cv:
            self._state()
            self._start_thread("command", self._command_loop)

    @property
    def microphone_enabled(self) -> bool:
        with self._cv:
            return self._microphone_enabled

    @property
    def voice_enabled(self) -> bool:
        with self._cv:
            return self._voice_enabled

    @property
    def busy(self) -> bool:
        with self._cv:
            return self._busy

    @property
    def closed(self) -> bool:
        with self._cv:
            return self._closed

    def drain_events(self) -> list[dict[str, Any]]:
        with self._cv:
            events = list(self._events)
            self._events.clear()
            return events

    def submit(self, text: str) -> bool:
        with self._cv:
            return self._submit(text)

    def _submit(self, text: str) -> bool:
        if self._closed:
            return False
        if not isinstance(text, str) or not text.strip():
            return False
        text = text.strip()
        if len(text) > self.MAX_TEXT_CHARS:
            self._error(f"Richiesta troppo lunga (massimo {self.MAX_TEXT_CHARS} caratteri).")
            return False
        if self._busy:
            self._error("Una richiesta è ancora in corso. Attendi il completamento.")
            return False
        self._turn += 1
        self._pending = (self._turn, text)
        self._busy = True
        self._clear_partial()
        self._invalidate_speech()
        self._emit({"type": "message", "role": "user", "text": text})
        self._state("Sto elaborando…")
        self._cv.notify_all()
        return True

    def toggle_microphone(self) -> bool:
        with self._cv:
            if self._closed:
                return False
            if self._sources["microphone"] is None:
                self._error("Microfono non disponibile.")
                return False
            self._microphone_enabled = not self._microphone_enabled
            self._mic_revision += 1
            self._clear_partial()
            self._request_stop("microphone")
            if self._microphone_enabled:
                self._start_thread("microphone", self._microphone_loop)
            self._state("Avvio microfono…" if self._microphone_enabled else "Microfono spento")
            self._cv.notify_all()
            return self._microphone_enabled

    def toggle_voice(self) -> bool:
        with self._cv:
            if self._closed:
                return False
            self._voice_enabled = not self._voice_enabled
            self._invalidate_speech()
            self._state("Voce attiva" if self._voice_enabled else "Voce disattivata")
            return self._voice_enabled

    def cancel(self) -> None:
        with self._cv:
            if self._closed:
                return
            self._turn += 1
            self._pending = None
            self._busy = self._running
            self._clear_partial()
            self._invalidate_speech()
            # Restart the callback generation so pre-cancel ASR cannot submit.
            self._mic_revision += 1
            if self._microphone_enabled:
                self._request_stop("microphone")
            self._state("Annullato; attendo fine richiesta" if self._busy else "Annullato")
            self._cv.notify_all()

    def close(self) -> None:
        with self._cv:
            if self._closed:
                return
            self._closed = True
            self._turn += 1
            self._mic_revision += 1
            self._voice_revision += 1
            self._microphone_enabled = False
            self._voice_enabled = False
            self._busy = False
            self._pending = self._partial = self._utterance = None
            self._events.clear()
            self._status = "Chiuso"
            self._events.append(self._state_event())
            for name in self._sources:
                if self._sources[name] is not None:
                    self._request_stop(name)
            self._cv.notify_all()

    def _start_thread(self, name, target) -> None:
        if name not in self._threads:
            def run():
                try:
                    target()
                finally:
                    with self._cv:
                        self._finished.add(name)
                        self._cv.notify_all()

            thread = Thread(target=run, name=f"franco-v7-{name}", daemon=True)
            self._threads[name] = thread
            thread.start()

    def _emit(self, event: dict[str, Any]) -> None:
        if self._closed:
            return
        if event["type"] in {"state", "partial"}:
            # Only the latest transient value is useful to a slow UI consumer.
            self._events = deque((old for old in self._events
                                  if old["type"] != event["type"]), maxlen=self.MAX_EVENTS)
        self._events.append(event)

    def _state_event(self) -> dict[str, Any]:
        return {"type": "state", "busy": self._busy,
                "microphone_enabled": self._microphone_enabled,
                "voice_enabled": self._voice_enabled, "status": self._status}

    def _state(self, status: str | None = None) -> None:
        if status is not None:
            self._status = status[:self.MAX_STATUS_CHARS]
        self._emit(self._state_event())

    def _error(self, text: str) -> None:
        self._emit({"type": "error", "text": text[:self.MAX_TEXT_CHARS]})

    def _clear_partial(self) -> None:
        self._partial = None
        self._emit({"type": "partial", "text": ""})

    def _invalidate_speech(self) -> None:
        self._voice_revision += 1
        self._utterance = None
        if self._sources["speech"] is not None:
            self._request_stop("speech")

    def _request_stop(self, name: str) -> None:
        self._stop_requested[name] += 1
        # Separate interrupt workers let a stuck device stop leave the other
        # device and command worker usable. There is at most one per device.
        self._start_thread(f"{name}-interrupt", lambda: self._interrupt_loop(name))
        self._cv.notify_all()

    def _resolve_device(self, name: str, method: str):
        with self._cv:
            if name in self._devices:
                return self._devices[name]
            source = self._sources[name]
        device = self._as_device(source, method)
        if not callable(getattr(device, method, None)):
            raise TypeError(f"Adattatore {name} non valido")
        with self._cv:
            self._devices[name] = device
            # A factory may finish after close; arrange cleanup without ever
            # starting the newly constructed device.
            if self._closed:
                self._request_stop(name)
            return device

    @staticmethod
    def _as_device(source, method: str):
        # A class or a plain callable is a zero-argument factory; only a real
        # instance already exposes the bound device methods.
        if not isinstance(source, type) and hasattr(source, method):
            return source
        return source()

    def _interrupt_loop(self, name: str) -> None:
        while True:
            with self._cv:
                self._cv.wait_for(lambda: self._stop_done[name] < self._stop_requested[name]
                                 or (self._closed and (name not in self._threads
                                                     or name in self._finished)))
                if self._stop_done[name] == self._stop_requested[name]:
                    return
                revision = self._stop_requested[name]
                device = self._devices.get(name)
                source = self._sources[name]
                if device is None and not isinstance(source, type) and hasattr(source, "stop"):
                    device = source
                closing = self._closed
            if device is not None:
                self._device_call(device, "stop", name)
                if closing and name not in self._device_closed:
                    self._device_call(device, "close", name)
                    with self._cv:
                        self._device_closed.add(name)
            with self._cv:
                self._stop_done[name] = revision
                self._cv.notify_all()

    def _device_call(self, device, method: str, name: str) -> None:
        try:
            callback = getattr(device, method, None)
            if callback is not None:
                callback()
        except Exception as exc:  # noqa: BLE001 - adapters are third-party boundaries
            with self._cv:
                self._error(f"Errore {name}: {exc}")

    def _command_loop(self) -> None:
        while True:
            with self._cv:
                self._cv.wait_for(lambda: self._closed or self._pending is not None
                                 or self._partial is not None)
                if self._closed:
                    return
                if self._pending is not None:
                    revision, text = self._pending
                    self._pending = None
                    self._running = True
                    final = True
                else:
                    revision, text = self._partial
                    self._partial = None
                    final = False
            if not final:
                try:
                    with self._cv:
                        valid = not self._closed and revision == self._mic_revision
                    if valid:
                        self.runtime.observe_partial(text)
                except Exception as exc:  # noqa: BLE001 - runtime boundary must survive
                    with self._cv:
                        if revision == self._mic_revision:
                            self._error(f"Preparazione richiesta non riuscita: {exc}")
                continue
            try:
                reply = self.runtime.submit_final(text)
                answer = str(getattr(reply, "text", reply) or "").strip()
                answer = answer[:self.MAX_TEXT_CHARS] or "Non ho ottenuto una risposta valida."
                with self._cv:
                    if not self._closed and revision == self._turn:
                        self._emit({"type": "message", "role": "assistant", "text": answer})
                        if self._voice_enabled and self._sources["speech"] is not None:
                            self._utterance = (revision, self._voice_revision, answer)
                            self._start_thread("speech", self._speech_loop)
                            self._cv.notify_all()
            except Exception as exc:  # noqa: BLE001 - runtime boundary must survive
                with self._cv:
                    if revision == self._turn:
                        self._error(f"Richiesta non riuscita: {exc}")
            finally:
                with self._cv:
                    self._running = False
                    self._busy = False
                    if not self._closed:
                        self._state("In ascolto" if self._microphone_enabled else "Pronto")
                    self._cv.notify_all()

    def _speech_loop(self) -> None:
        while True:
            with self._cv:
                self._cv.wait_for(lambda: self._closed or self._utterance is not None)
                if self._closed:
                    return
                utterance = self._utterance
                self._utterance = None
            try:
                device = self._resolve_device("speech", "say")
                with self._cv:
                    self._cv.wait_for(lambda: self._closed or self._stop_done["speech"]
                                     == self._stop_requested["speech"])
                    valid = (not self._closed and self._voice_enabled
                             and utterance[:2] == (self._turn, self._voice_revision))
                if valid:
                    device.say(utterance[2])
                    with self._cv:
                        if self._closed or utterance[:2] != (self._turn, self._voice_revision):
                            self._request_stop("speech")
            except Exception as exc:  # noqa: BLE001 - speech adapter boundary
                with self._cv:
                    if utterance[:2] == (self._turn, self._voice_revision):
                        self._error(f"Voce non disponibile: {exc}")

    def _microphone_loop(self) -> None:
        handled = -1
        while True:
            with self._cv:
                self._cv.wait_for(
                    lambda handled=handled: self._closed or self._mic_revision != handled
                )
                if self._closed:
                    return
                handled = self._mic_revision
                if not self._microphone_enabled:
                    continue
            try:
                device = self._resolve_device("microphone", "start")
                with self._cv:
                    self._cv.wait_for(lambda: self._closed or self._stop_done["microphone"]
                                     == self._stop_requested["microphone"])
                    if not self._valid_microphone(handled):
                        continue
                device.start(
                    on_partial=lambda text, rev=handled: self._on_partial(rev, text),
                    on_final=lambda text, rev=handled: self._on_final(rev, text),
                    on_status=lambda status, rev=handled: self._on_status(rev, status),
                )
                with self._cv:
                    if not self._valid_microphone(handled):
                        self._request_stop("microphone")
            except Exception as exc:  # noqa: BLE001 - microphone adapter boundary
                with self._cv:
                    if self._valid_microphone(handled):
                        self._microphone_enabled = False
                        self._mic_revision += 1
                        self._clear_partial()
                        self._request_stop("microphone")
                        self._error(f"Microfono non disponibile: {exc}")
                        self._state("Microfono non disponibile")

    def _valid_microphone(self, revision: int) -> bool:
        return (not self._closed and self._microphone_enabled
                and revision == self._mic_revision)

    def _on_partial(self, revision: int, text: str) -> None:
        with self._cv:
            if not self._valid_microphone(revision) or not isinstance(text, str):
                return
            text = text.strip()[:self.MAX_PARTIAL_CHARS]
            self._partial = (revision, text)
            self._emit({"type": "partial", "text": text})
            self._cv.notify_all()

    def _on_final(self, revision: int, text: str) -> None:
        with self._cv:
            if self._valid_microphone(revision):
                self._clear_partial()
                self._submit(text)

    def _on_status(self, revision: int, status) -> None:
        with self._cv:
            if not self._valid_microphone(revision):
                return
            if isinstance(status, dict):
                error = status.get("error")
                is_error = (status.get("type") == "error"
                            or status.get("status") == "error")
                if error or is_error:
                    self._error(str(error or status.get("text") or "Errore microfono"))
                    self._microphone_enabled = False
                    self._mic_revision += 1
                    self._clear_partial()
                    self._request_stop("microphone")
                    self._state("Microfono non disponibile")
                    return
                status = status.get("status", status.get("text", ""))
            if isinstance(status, str) and status:
                self._state(status)
