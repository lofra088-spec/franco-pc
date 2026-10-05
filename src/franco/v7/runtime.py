"""Conversation-first coordinator for the rebuilt Franco V7."""
from __future__ import annotations

import time
from collections import deque
from dataclasses import dataclass

from .actions import ActionRegistry
from .contracts import Brain, PreparedTurn
from .intent import IntentParser, normalize


@dataclass(frozen=True)
class RuntimeReply:
    text: str
    intent: str
    executed: bool


class FrancoRuntime:
    """Consumes partial speech safely and executes only the final transcript."""

    def __init__(self, brain: Brain, actions: ActionRegistry | None = None):
        self.brain = brain
        self.actions = actions or ActionRegistry()
        self.parser = IntentParser()
        self.prepared: PreparedTurn | None = None
        self.history: deque[dict[str, str]] = deque(maxlen=16)
        self._brain_failures = 0
        self._brain_blocked_until = 0.0

    def observe_partial(self, transcript: str) -> PreparedTurn:
        """Think ahead from interim ASR without producing side effects."""
        text = normalize(transcript)
        self.prepared = PreparedTurn(text, self.parser.parse(text), is_final=False)
        return self.prepared

    def submit_final(self, transcript: str) -> RuntimeReply:
        text = normalize(transcript)
        intent = self.parser.parse(text)
        self.prepared = PreparedTurn(text, intent, is_final=True)
        if intent.name == "empty":
            return RuntimeReply("Non ho sentito una richiesta completa.", "empty", False)
        if intent.name == "confirm":
            return RuntimeReply(self.actions.confirm(), "confirm", True)
        if intent.name == "cancel":
            return RuntimeReply(self.actions.cancel(), "cancel", True)
        if self.actions.has(intent.name):
            try:
                text = self.actions.execute(intent)
            except Exception as exc:  # noqa: BLE001 - actions are extension boundaries
                return RuntimeReply(
                    f"Non ho completato l'azione: {exc}", intent.name, False,
                )
            return RuntimeReply(text, intent.name, True)

        if time.monotonic() < self._brain_blocked_until:
            return RuntimeReply(
                "Il servizio AI è temporaneamente isolato dopo più errori; i comandi locali restano disponibili.",
                "conversation", False,
            )
        try:
            answer = self.brain.answer(text, context=list(self.history)[-8:])
            self._brain_failures = 0
        except Exception:  # noqa: BLE001 - provider failures must not crash the assistant
            self._brain_failures += 1
            if self._brain_failures >= 3:
                self._brain_blocked_until = time.monotonic() + 30
            return RuntimeReply(
                "Non ho ottenuto una risposta dal modello. I comandi locali continuano a funzionare.",
                "conversation", False,
            )
        answer = str(answer or "").strip() or "Non ho ottenuto una risposta valida."
        self.history.extend(({"role": "user", "content": text},
                             {"role": "assistant", "content": answer}))
        return RuntimeReply(answer, "conversation", False)
