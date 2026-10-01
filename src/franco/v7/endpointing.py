"""Adaptive end-of-turn detection for natural Italian speech."""
from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class EndpointDecision:
    should_finalize: bool
    wait_seconds: float
    reason: str


class AdaptiveEndpointDetector:
    """Waits longer for visibly unfinished thoughts and fillers."""

    def __init__(self, complete_pause: float = .85, uncertain_pause: float = 2.0,
                 truncated_pause: float = 5.0):
        self.complete_pause = complete_pause
        self.uncertain_pause = uncertain_pause
        self.truncated_pause = truncated_pause

    @staticmethod
    def _looks_truncated(text: str) -> bool:
        low = re.sub(r"\s+", " ", (text or "").strip().casefold())
        if not low:
            return True
        trailing = (
            "e", "o", "ma", "però", "perche", "perché", "che", "se", "quando",
            "mentre", "quindi", "tipo", "cioè", "allora", "poi", "con", "senza",
            "per", "di", "da", "a", "il", "lo", "la", "un", "una",
        )
        last = re.sub(r"[^a-zà-ù]+", "", low.split()[-1])
        if last in trailing:
            return True
        return low.endswith(("...", "-")) or bool(re.search(r"\b(?:ehm+|mmm+|aspetta)\s*$", low))

    def decide(self, text: str, silence_seconds: float) -> EndpointDecision:
        silence = max(0.0, float(silence_seconds))
        words = re.findall(r"\w+", text or "", flags=re.UNICODE)
        if self._looks_truncated(text):
            wait = self.truncated_pause
            reason = "frase_troncata"
        elif len(words) <= 2:
            wait = self.uncertain_pause
            reason = "frase_breve"
        else:
            wait = self.complete_pause
            reason = "frase_completa"
        return EndpointDecision(silence >= wait, max(0.0, wait - silence), reason)

