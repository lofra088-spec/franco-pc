"""franco.core.events — lightweight async pub/sub event bus.

Dependency-free and importable without the monolith. Async components (the
cyber subsystem in particular) publish `Event` objects through
`EventBus.emit`; both sync and coroutine subscribers are supported and event
names are matched with shell-style wildcards ("cyber.*", "cyber.recon.*").

The historical *synchronous* bus is untouched and still lives at
`franco._monolith.EventBus` for legacy callers.
"""
from __future__ import annotations

import fnmatch
import inspect
import logging
import time
from collections import defaultdict, deque
from enum import IntEnum
from typing import Any, Callable

logger = logging.getLogger(__name__)

__all__ = ["Priority", "Event", "EventBus"]


class Priority(IntEnum):
    """Dispatch priority — higher runs first."""
    LOWEST = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    HIGHEST = 5
    CRITICAL = 6


class Event:
    """An emitted event.

    Constructed as ``Event("cyber.recon.active.start", target=host)`` — the
    first positional is the dotted name; ``priority`` and ``source`` are
    reserved keywords, every other keyword lands in ``payload`` and is also
    reachable as an attribute (``event.target``).
    """

    __slots__ = ("name", "priority", "source", "timestamp", "payload")

    def __init__(self, name: str, *, priority: Priority = Priority.NORMAL,
                 source: str = "system", **payload: Any) -> None:
        self.name = name
        self.priority = priority
        self.source = source
        self.timestamp = time.time()
        self.payload = payload

    def __getattr__(self, item: str) -> Any:
        # only reached for names not in __slots__
        try:
            return self.payload[item]
        except KeyError as exc:
            raise AttributeError(item) from exc

    def get(self, key: str, default: Any = None) -> Any:
        return self.payload.get(key, default)

    def __repr__(self) -> str:
        return f"Event({self.name!r}, priority={self.priority.name}, payload={self.payload!r})"


class EventBus:
    """Async pub/sub bus with wildcard topics."""

    def __init__(self) -> None:
        self._subs: dict[str, list[tuple[Callable, Priority]]] = defaultdict(list)
        self._history: deque[Event] = deque(maxlen=500)
        self._stats: dict[str, int] = defaultdict(int)

    def subscribe(self, pattern: str, callback: Callable,
                  priority: Priority = Priority.NORMAL) -> Callable:
        """Register ``callback`` for events matching ``pattern`` ("cyber.*")."""
        self._subs[pattern].append((callback, priority))
        self._subs[pattern].sort(key=lambda cp: cp[1], reverse=True)
        return callback

    def on(self, pattern: str, priority: Priority = Priority.NORMAL) -> Callable:
        """Decorator form of :meth:`subscribe`."""
        def deco(fn: Callable) -> Callable:
            self.subscribe(pattern, fn, priority)
            return fn
        return deco

    def unsubscribe(self, pattern: str, callback: Callable) -> None:
        self._subs[pattern] = [
            (cb, p) for cb, p in self._subs.get(pattern, []) if cb != callback
        ]

    async def emit(self, event: "Event | str", **payload: Any) -> Event:
        """Emit an :class:`Event` (or a bare name) to all matching subscribers.

        Subscriber exceptions are logged, never propagated — one bad handler
        must not sink an operation.
        """
        if isinstance(event, str):
            event = Event(event, **payload)

        self._history.append(event)
        self._stats[event.name] += 1

        matched: list[tuple[Callable, Priority]] = []
        for pattern, subs in self._subs.items():
            if fnmatch.fnmatch(event.name, pattern):
                matched.extend(subs)
        matched.sort(key=lambda cp: cp[1], reverse=True)

        for callback, _prio in matched:
            try:
                result = callback(event)
                if inspect.isawaitable(result):
                    await result
            except Exception as exc:  # noqa: BLE001 — isolate handlers
                logger.warning("event subscriber failed on %s: %s", event.name, exc)

        return event

    @property
    def history(self) -> list[Event]:
        return list(self._history)

    def stats(self) -> dict[str, int]:
        return dict(self._stats)
