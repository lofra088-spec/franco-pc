"""Deterministic intent recognition for commands that must feel instant."""
from __future__ import annotations

import re
import unicodedata

from .contracts import Intent


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.replace("’", "'")
    return re.sub(r"\s+", " ", text).strip()


class IntentParser:
    """Parses local actions first and leaves open conversation to the brain."""

    _OPEN = re.compile(r"^(?:ehi franco[, ]*)?(?:apri|avvia|lancia)\s+(.+)$", re.I)
    _SEARCH = re.compile(
        r"^(?:ehi franco[, ]*)?(?:cerca|cercami|trova|trovami|googla)"
        r"(?:\s+su google|\s+online|\s+sul web)?\s+(.+)$", re.I,
    )
    _DESKTOP = re.compile(
        r"^(?:franco code\s+)?(?:usa\s+)?computer use\s*(?:per|:|-)?\s*(.+)$", re.I,
    )

    def parse(self, text: str) -> Intent:
        clean = normalize(text)
        if not clean:
            return Intent("empty", confidence=1.0)
        if clean.casefold().strip(" ,.!?") in {
            "franco mappa", "apri franco mappa", "apri la mappa",
            "mostra la mappa del mondo", "mappa mondiale",
        }:
            return Intent("world_map", confidence=1.0)
        match = self._DESKTOP.match(clean)
        if match:
            return Intent("desktop_goal", {"goal": match.group(1).strip()}, .98)
        match = self._OPEN.match(clean)
        if match:
            return Intent("open_app", {"name": match.group(1).strip(" .")}, .99)
        match = self._SEARCH.match(clean)
        if match:
            return Intent("web_search", {"query": match.group(1).strip()}, .99)
        lowered = clean.lower()
        if lowered in {"conferma", "confermo", "conferma azione"}:
            return Intent("confirm", confidence=1.0)
        if lowered in {"annulla", "stop", "fermati", "annulla azione"}:
            return Intent("cancel", confidence=1.0)
        return Intent("conversation", {"text": clean}, .75)
