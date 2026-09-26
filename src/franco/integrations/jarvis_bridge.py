"""Jarvis compatibility bridge for the FRANCO runtime.

The bridge deliberately reuses FRANCO's provider router and XTTS service. It
does not import the Electron client, so the Python application remains usable
without Node or an OpenAI SDK. OpenRouter is the only cloud provider used by
this compatibility surface.
"""
from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Callable

from ..model_router import LatencyRouter, environment_providers
from .jarvis_services import JarvisServices


class JarvisBridge:
    """Expose Jarvis-style chat and voice operations inside FRANCO."""

    def __init__(self, logger: Any = None, providers: dict[str, Callable[..., str]] | None = None):
        self.logger = logger
        self.router = LatencyRouter(providers or environment_providers(), logger=logger)
        self.services = JarvisServices()
        self.xtts_url = os.getenv("FRANCO_XTTS_URL", "http://127.0.0.1:8790").rstrip("/")

    def chat(self, text: str, system: str | None = None, **kwargs: Any) -> str:
        """Answer through OpenRouter/Groq according to FRANCO's latency policy."""
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Il messaggio Jarvis non può essere vuoto")
        if len(text) > 12000:
            raise ValueError("Il messaggio Jarvis supera 12000 caratteri")
        return self.router.chat(text.strip(), system=system, **kwargs)

    def speak(self, text: str, speaker: str | None = None, language: str = "it") -> bytes:
        """Request WAV audio from the already supervised local XTTS server."""
        if not isinstance(text, str) or not text.strip() or len(text) > 6000:
            raise ValueError("Il testo vocale deve contenere da 1 a 6000 caratteri")
        payload = {"text": text.strip(), "language": language}
        if speaker:
            payload["speaker"] = speaker
        request = urllib.request.Request(
            self.xtts_url + "/tts",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=180) as response:
            audio = response.read(12_000_000)
        if not audio.startswith(b"RIFF"):
            raise RuntimeError("XTTS ha restituito un audio non valido")
        return audio


__all__ = ["JarvisBridge"]
