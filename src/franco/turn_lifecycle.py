"""Bounded request ownership, cooperative cancellation and timeout notification."""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass, field
import math
import threading
import time
import uuid


@dataclass
class Turn:
    id: str
    command: str
    started: float
    deadline: float
    status: str = "running"
    cancel_event: threading.Event = field(default_factory=threading.Event, repr=False)


class TurnLifecycle:
    def __init__(self, timeout_callback, timeout=60, clock=time.monotonic):
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("Il timeout deve essere positivo e finito")
        self.timeout_callback, self.timeout, self._clock = timeout_callback, timeout, clock
        self._lock = threading.RLock()
        self._turns = {}
        self._history = deque(maxlen=64)
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._watch, daemon=True, name="TurnWatchdog")
        self._thread.start()

    def begin(self, command):
        now = self._clock()
        turn = Turn(uuid.uuid4().hex, command, now, now + self.timeout)
        with self._lock:
            if self._stop.is_set():
                raise RuntimeError("Franco si sta chiudendo")
            if len(self._turns) >= 8:
                raise RuntimeError("Troppi lavori ancora in corso")
            self._turns[turn.id] = turn
        return turn.id

    def token(self, turn_id):
        with self._lock:
            turn = self._turns.get(turn_id)
            if turn:
                return turn.cancel_event
        stopped = threading.Event()
        stopped.set()
        return stopped

    def is_active(self, turn_id):
        with self._lock:
            turn = self._turns.get(turn_id)
            return bool(turn and turn.status == "running" and not turn.cancel_event.is_set())

    def _record(self, turn):
        self._history.append({"id": turn.id, "status": turn.status,
                              "elapsed_s": round(self._clock() - turn.started, 3)})

    def finish(self, turn_id, status="complete"):
        with self._lock:
            turn = self._turns.pop(turn_id, None)
            if not turn:
                return False
            valid = turn.status == "running" and not turn.cancel_event.is_set()
            if valid:
                turn.status = status
            self._record(turn)
            return valid

    def cancel(self, turn_id=None):
        with self._lock:
            turns = ([self._turns[turn_id]] if turn_id in self._turns else []) if turn_id else list(self._turns.values())
            for turn in turns:
                turn.cancel_event.set()
                turn.status = "cancelled"

    def check_timeouts(self):
        expired = []
        with self._lock:
            now = self._clock()
            for turn in self._turns.values():
                if turn.status == "running" and now >= turn.deadline:
                    turn.status = "timed_out"
                    turn.cancel_event.set()
                    expired.append(turn)
        for turn in expired:
            try:
                self.timeout_callback(turn)
            except Exception:
                pass

    def metrics(self):
        with self._lock:
            return list(self._history)

    def _watch(self):
        while not self._stop.wait(.25):
            self.check_timeouts()

    def stop(self):
        self.cancel()
        self._stop.set()
        if self._thread is not threading.current_thread():
            self._thread.join(timeout=1)
