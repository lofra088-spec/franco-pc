"""Bounded screenshot-action loop for authorized Windows desktop goals."""
from __future__ import annotations

import base64
import json
import re
import time
from io import BytesIO
from threading import Event, Lock, Thread

SYSTEM_PROMPT = (
    "Sei il controller visuale di Franco V7 sul PC autorizzato dell'utente. "
    "Osserva lo screenshot e scegli UNA sola azione. Non aprire terminali, PowerShell, "
    "prompt, finestre di autenticazione o impostazioni di sicurezza. Per inviare, "
    "pubblicare, comprare, cancellare, caricare file, stampare, avviare una live o "
    "confermare un'azione esterna usa action=confirm con next_action. Rispondi solo JSON: "
    '{"action":"click","x":1,"y":1,"reason":"..."}, '
    '{"action":"double_click","x":1,"y":1,"reason":"..."}, '
    '{"action":"key","key":"ctrl+l","reason":"..."}, '
    '{"action":"type","text":"...","reason":"..."}, '
    '{"action":"wait","reason":"..."}, '
    '{"action":"confirm","reason":"...","next_action":{"action":"click","x":1,"y":1}}, '
    'oppure {"action":"done","reason":"obiettivo verificato o impossibile"}.'
)

SENSITIVE_GOAL_WORDS = (
    "invia", "pubblica", "compra", "acquista", "cancella", "elimina", "carica",
    "upload", "stampa", "avvia live", "avvia trasmissione", "login", "accedi",
    "password", "paga", "bonifico",
)


class DesktopAgent:
    MAX_STEPS = 30
    MAX_SECONDS = 10 * 60

    def __init__(self, brain, *, automation=None, step_pause: float = .8):
        self.brain = brain
        self._automation = automation
        self.step_pause = step_pause
        self._lock = Lock()
        self._stop = Event()
        self._confirmation = Event()
        self._pending = None
        self._pending_goal = None
        self._thread = None
        self._status = "Computer Use inattivo."

    def start(self, goal: str) -> str:
        goal = " ".join(str(goal or "").split()).strip()
        if not goal:
            return "Dimmi quale obiettivo deve completare Computer Use."
        if any(word in goal.casefold() for word in SENSITIVE_GOAL_WORDS):
            with self._lock:
                if self._thread and self._thread.is_alive():
                    return "Computer Use sta gia' lavorando."
                self._pending_goal = goal
                self._status = f"Serve conferma per avviare: {goal}"
            return (f"Serve conferma prima di avviare questo obiettivo: {goal}. "
                    "Di' 'conferma computer use' oppure 'ferma computer use'.")
        return self._begin(goal)

    def _begin(self, goal: str) -> str:
        automation = self._get_automation()
        with self._lock:
            if self._thread and self._thread.is_alive():
                return "Computer Use sta gia' lavorando."
            self._stop = Event()
            self._confirmation = Event()
            self._pending = None
            self._pending_goal = None
            self._status = f"Computer Use sta lavorando su: {goal}"
            self._thread = Thread(target=self._run, args=(goal, automation), daemon=True,
                                  name="FrancoV7-ComputerUse")
            self._thread.start()
        return (f"Computer Use ha preso l'obiettivo: {goal}. "
                "Controlla lo schermo a ogni passo e puoi fermarlo dicendo 'ferma computer use'.")

    def stop(self) -> str:
        self._stop.set()
        self._confirmation.set()
        with self._lock:
            active = bool(self._thread and self._thread.is_alive())
            self._pending_goal = None
            self._status = "Computer Use si sta fermando." if active else "Computer Use inattivo."
        return self._status

    def confirm(self) -> str:
        with self._lock:
            goal, self._pending_goal = self._pending_goal, None
            if goal is None and self._pending is None:
                return "Computer Use non ha azioni in attesa di conferma."
        if goal is not None:
            return self._begin(goal)
        with self._lock:
            if self._pending is None:
                return "Computer Use non ha azioni in attesa di conferma."
        self._confirmation.set()
        return "Conferma ricevuta. Computer Use riprende."

    def status(self) -> str:
        with self._lock:
            return self._status

    def _get_automation(self):
        if self._automation is not None:
            return self._automation
        try:
            import pyautogui
        except ImportError as exc:
            raise RuntimeError("Computer Use richiede pyautogui e Pillow.") from exc
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = .05
        self._automation = pyautogui
        return pyautogui

    def _run(self, goal, automation):
        started = time.monotonic()
        outcome = "Computer Use ha raggiunto il limite di passi."
        try:
            for step in range(1, self.MAX_STEPS + 1):
                if self._stop.is_set() or time.monotonic() - started > self.MAX_SECONDS:
                    outcome = "Computer Use e' stato fermato."
                    break
                image = self._capture(automation)
                raw = self.brain.decide_screen(
                    f"Obiettivo: {goal}\nPasso {step}. Decidi la prossima azione.",
                    image, system=SYSTEM_PROMPT,
                )
                data = self._parse(raw)
                if not isinstance(data, dict):
                    outcome = "Computer Use ha ricevuto un piano non valido."
                    break
                action = str(data.get("action", "wait")).casefold()
                reason = str(data.get("reason", "")).strip()
                if action in {"done", "fine", "stop"}:
                    outcome = reason or "Obiettivo completato e verificato."
                    break
                if action in {"confirm", "conferma"}:
                    with self._lock:
                        self._pending = data
                        self._status = "Serve conferma: " + (reason or "azione esterna")
                    self._confirmation.clear()
                    if not self._confirmation.wait(120) or self._stop.is_set():
                        outcome = "Computer Use si e' fermato in attesa di conferma."
                        break
                    with self._lock:
                        pending, self._pending = self._pending, None
                    next_action = pending.get("next_action") if isinstance(pending, dict) else None
                    if not isinstance(next_action, dict):
                        outcome = "L'azione confermata non era valida."
                        break
                    self._execute(automation, next_action)
                else:
                    self._execute(automation, data)
                if self._stop.wait(self.step_pause):
                    outcome = "Computer Use e' stato fermato."
                    break
        except Exception as exc:  # noqa: BLE001 - native input and provider boundary
            outcome = f"Computer Use si e' fermato: {exc}"
        finally:
            with self._lock:
                self._pending = None
                self._status = outcome
                self._thread = None

    @staticmethod
    def _capture(automation) -> str:
        image = automation.screenshot()
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode("ascii")

    @staticmethod
    def _parse(raw):
        match = re.search(r"\{.*\}", str(raw or ""), re.DOTALL)
        if not match:
            return None
        try:
            return json.loads(match.group())
        except ValueError:
            return None

    @staticmethod
    def _execute(automation, data):
        action = str(data.get("action", "wait")).casefold()
        if action == "click":
            automation.click(x=int(data["x"]), y=int(data["y"]))
        elif action in {"double_click", "doppio_click"}:
            automation.doubleClick(x=int(data["x"]), y=int(data["y"]))
        elif action in {"key", "tasto"}:
            keys = [part.strip().casefold() for part in str(data.get("key", "")).split("+")]
            if not keys or len(keys) > 4 or not all(re.fullmatch(r"[a-z0-9_]+", key) for key in keys):
                raise ValueError("tasto non valido")
            automation.hotkey(*keys) if len(keys) > 1 else automation.press(keys[0])
        elif action in {"type", "scrivi"}:
            text = str(data.get("text", data.get("testo", "")))[:2000]
            if not text:
                raise ValueError("testo mancante")
            automation.write(text, interval=.01)
        elif action in {"wait", "attendi"}:
            return
        else:
            raise ValueError(f"azione non consentita: {action}")
