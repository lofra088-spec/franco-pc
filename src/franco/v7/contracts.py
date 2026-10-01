"""Small interfaces shared by the V7 runtime."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Protocol


class Brain(Protocol):
    def answer(self, text: str, *, context: list[dict[str, str]]) -> str: ...


class Action(Protocol):
    def __call__(self, **arguments: Any) -> str: ...


@dataclass(frozen=True)
class Intent:
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)
    confidence: float = 1.0
    requires_confirmation: bool = False


@dataclass(frozen=True)
class PreparedTurn:
    transcript: str
    intent: Intent
    is_final: bool = False


ActionFactory = Callable[..., str]

