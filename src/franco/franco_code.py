"""Franco Code: persistent goal orchestration for desktop/background work.

The pod exposes a small state machine rather than the assistant's private
reasoning. It can be fed by voice, chat, or an automation and persists its
current goal so a restart can resume safely.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path
import threading
import time
import uuid


@dataclass
class PodState:
    goal: str = ""
    phase: str = "idle"
    detail: str = ""
    last_update: str = ""
    status: str = "idle"  # idle, running, paused, done, error, stopped
    step: int = 0
    total_steps: int = 0
    error: str = ""
    notifications: list[str] = field(default_factory=list)
    plan: list[str] = field(default_factory=list)
    results: list[str] = field(default_factory=list)
    retries: int = 0
    confirmation_required: bool = False
    confirmation_granted: bool = False
    report_ready: bool = False


class FrancoCode:
    """Background goal runner with pause/stop and atomic state persistence."""

    def __init__(self, data_dir, logger=None, announce=None, ui_state=None,
                 complete_notify=None):
        self.path = Path(data_dir) / "franco_code.json"
        legacy = Path(data_dir) / "franco_pod.json"
        if not self.path.exists() and legacy.exists():
            try:
                legacy.replace(self.path)
            except OSError:
                pass
        self.logger = logger
        self.announce = announce or (lambda _message: None)
        self.ui_state = ui_state
        self.complete_notify = complete_notify or (lambda _message: None)
        self._lock = threading.RLock()
        self._stop = threading.Event()
        self._pause = threading.Event()
        self._thread = None
        self.state = self._load()

    def _load(self):
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            return PodState(**{k: raw[k] for k in PodState.__dataclass_fields__ if k in raw})
        except (OSError, ValueError, TypeError):
            return PodState()

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(asdict(self.state), ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(self.path)
        if self.ui_state is not None:
            try:
                self.ui_state.set("franco_code", asdict(self.state), notify=False)
            except Exception:
                pass

    def snapshot(self):
        with self._lock:
            return asdict(self.state)

    def _notify(self, message, speak=False):
        with self._lock:
            self.state.last_update = datetime.now(timezone.utc).isoformat(timespec="seconds")
            self.state.notifications = (self.state.notifications + [message])[-20:]
            self._save()
        if speak:
            try:
                self.announce(message)
            except Exception:
                pass

    @staticmethod
    def _needs_confirmation(text):
        risky = ("invia", "pubblica", "elimina", "cancella dati", "acquista", "compra",
                 "pagamento", "prenota", "manda email", "manda un messaggio",
                 "modifica permessi", "cambia password", "account")
        lowered = text.lower()
        return any(word in lowered for word in risky)

    def start(self, goal, steps, worker):
        goal = str(goal or "").strip()
        if not goal:
            raise ValueError("L'obiettivo non può essere vuoto")
        if self._thread and self._thread.is_alive():
            raise RuntimeError("Franco Code sta già lavorando")
        steps = list(steps or [])
        if not steps:
            raise ValueError("Serve almeno un passo operativo")
        self._stop.clear()
        self._pause.clear()
        with self._lock:
            self.state = PodState(goal=goal, phase="preparazione", detail="Piano creato",
                                  status="running", total_steps=len(steps), plan=steps)
            self._save()
        self._thread = threading.Thread(target=self._run, args=(steps, worker),
                                        daemon=True, name="FrancoCode")
        self._thread.start()

    def resume_pending(self, worker):
        with self._lock:
            if self.state.status not in ("running", "paused", "waiting_confirmation") or not self.state.plan:
                return False
            if self.state.status == "paused":
                self._pause.set()
            if self.state.status == "waiting_confirmation" and not self.state.confirmation_granted:
                return False
            self.state.status = "running"
            self._save()
            plan = list(self.state.plan)
        self._thread = threading.Thread(target=self._run, args=(plan, worker),
                                        daemon=True, name="FrancoCodeResume")
        self._thread.start()
        return True

    def confirm_and_resume(self, worker):
        with self._lock:
            self.state.confirmation_granted = True
            self.state.confirmation_required = False
            self.state.status = "running"
            self._save()
        return self.resume_pending(worker)

    def _run(self, steps, worker):
        try:
            start_at = max(1, int(self.state.step or 1))
            for index, step in enumerate(steps, 1):
                if index < start_at:
                    continue
                while self._pause.is_set() and not self._stop.is_set():
                    time.sleep(.2)
                if self._stop.is_set():
                    break
                if (self._needs_confirmation(self.state.goal + " " + step)
                        and not self.state.confirmation_granted):
                    with self._lock:
                        self.state.status = "waiting_confirmation"
                        self.state.phase = "richiede conferma"
                        self.state.confirmation_required = True
                        self._save()
                    self._notify("Franco Code richiede una conferma prima dell'azione esterna o irreversibile.", speak=True)
                    return
                with self._lock:
                    self.state.step, self.state.phase, self.state.detail = index, "esecuzione", str(step)
                    self._save()
                self._notify(f"Franco Code: avvio fase {index} di {len(steps)}.", speak=True)
                result, last_error = False, ""
                for attempt in range(3):
                    try:
                        result = worker(step, self._stop)
                        if result is not False:
                            break
                        last_error = "controllo interno non superato"
                    except Exception as error:
                        last_error = str(error)
                    with self._lock:
                        self.state.retries += 1
                        self.state.detail = f"Riprovo la fase {index}: {last_error}"
                        self._save()
                    if attempt < 2:
                        self._stop.wait(1.5 * (attempt + 1))
                if result is False:
                    raise RuntimeError(f"Fase {index} non completata dopo 3 tentativi: {last_error}")
                with self._lock:
                    self.state.results.append(f"Fase {index}: completata")
                    self._save()
                self._notify(f"Franco Code: fase {index} completata e controllata.", speak=True)
            with self._lock:
                self.state.status = "stopped" if self._stop.is_set() else "done"
                self.state.phase = "interrotto" if self._stop.is_set() else "completato"
                self.state.detail = ""
                self.state.report_ready = True
                self._save()
            final_message = ("Franco Code: obiettivo completato. Vuoi il report?"
                             if not self._stop.is_set() else "Franco Code: lavoro fermato. Vuoi il report?")
            self._notify(final_message, speak=True)
            self.complete_notify(final_message)
        except Exception as exc:
            with self._lock:
                self.state.status, self.state.phase, self.state.error = "error", "errore", str(exc)
                self._save()
            self._notify(f"Franco Code: errore, {exc}", speak=True)
            self.complete_notify("Franco Code è bloccato. Vuoi il report?")

    def pause(self):
        self._pause.set()
        with self._lock:
            self.state.status, self.state.phase = "paused", "in pausa"
            self._save()
        self._notify("Franco Code: messo in pausa", speak=True)

    def resume(self):
        self._pause.clear()
        with self._lock:
            if self.state.status == "paused":
                self.state.status, self.state.phase = "running", "ripresa"
                self._save()
        self._notify("Franco Code: lavoro ripreso", speak=True)

    def stop(self):
        self._stop.set()
        self._pause.clear()

    def clear(self):
        self.stop()
        with self._lock:
            self.state = PodState()
            self._save()

    def report(self) -> str:
        snap = self.snapshot()
        if not snap.get("goal"):
            return "Non c'è ancora un report di Franco Code."
        lines = ["Report Franco Code", f"Obiettivo: {snap['goal']}",
                 f"Esito: {snap['status']}",
                 f"Progresso: {snap['step']} di {snap['total_steps']}"]
        if snap.get("results"):
            lines.append("Passi: " + "; ".join(snap["results"]))
        if snap.get("error"):
            lines.append("Problema: " + snap["error"])
        lines.append(f"Tentativi aggiuntivi: {snap.get('retries', 0)}")
        return "\n".join(lines)
