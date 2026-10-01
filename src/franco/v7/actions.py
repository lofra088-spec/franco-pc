"""Action registry with one confirmation gate for consequential operations."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from .contracts import Intent


@dataclass
class PendingAction:
    intent: Intent
    description: str


class ActionRegistry:
    def __init__(self):
        self._handlers: dict[str, Callable[..., str]] = {}
        self.pending: PendingAction | None = None

    def register(self, name: str, handler: Callable[..., str]) -> None:
        self._handlers[name] = handler

    def has(self, name: str) -> bool:
        return name in self._handlers

    def execute(self, intent: Intent) -> str:
        handler = self._handlers.get(intent.name)
        if handler is None:
            raise LookupError(intent.name)
        if intent.requires_confirmation:
            self.pending = PendingAction(intent, f"Eseguire {intent.name}")
            return f"Serve conferma prima di: {self.pending.description}."
        return str(handler(**intent.arguments))

    def confirm(self) -> str:
        if self.pending is None:
            return "Non c'è alcuna azione in attesa."
        pending, self.pending = self.pending, None
        handler = self._handlers.get(pending.intent.name)
        if handler is None:
            return "L'azione preparata non è più disponibile."
        return str(handler(**pending.intent.arguments))

    def cancel(self) -> str:
        self.pending = None
        return "Azione annullata."

