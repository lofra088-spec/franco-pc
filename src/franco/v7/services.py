"""Dependency-light adapters used by the clean V7 runtime."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request
import webbrowser


class OpenRouterBrain:
    """Small OpenAI-compatible client; no SDK is loaded into RAM."""

    endpoint = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = (api_key or os.getenv("OPENROUTER_API_KEY", "")).strip()
        self.model = model or os.getenv("FRANCO_OPENROUTER_MODEL", "openrouter/auto")

    def answer(self, text: str, *, context: list[dict[str, str]]) -> str:
        if not self.api_key:
            raise RuntimeError("OPENROUTER_API_KEY non configurata")
        system = {
            "role": "system",
            "content": (
                "Sei Franco 7, assistente operativo personale. Rispondi in italiano naturale, "
                "breve e concreto. Interpreta con buon senso gli errori di trascrizione. "
                "Non dichiarare mai di avere eseguito un'azione se non ricevi un esito reale."
            ),
        }
        payload = json.dumps({
            "model": self.model,
            "messages": [system, *context, {"role": "user", "content": text}],
            "temperature": .35,
            "max_tokens": 600,
        }).encode("utf-8")
        request = urllib.request.Request(
            self.endpoint, data=payload, method="POST",
            headers={"Authorization": f"Bearer {self.api_key}",
                     "Content-Type": "application/json", "X-Title": "Franco 7"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.load(response)
        return str(data["choices"][0]["message"].get("content") or "").strip()


class WindowsActions:
    """Fast local actions without loading the legacy application."""

    def __init__(self):
        self._known = {
            "chrome": ("process", ["chrome.exe"]),
            "discord": ("uri", "discord:"),
            "obs": ("process", ["obs64.exe"]),
        }

    def open_app(self, name: str) -> str:
        clean = name.casefold().strip()
        target = next((value for key, value in self._known.items() if key in clean), None)
        if target is None:
            # Windows resolves registered applications without a shell command
            # interpreter and reports failure immediately when no target exists.
            candidate = Path(name).expanduser()
            if candidate.is_file():
                os.startfile(str(candidate))
                return f"Apro {candidate.name}."
            raise LookupError(f"Applicazione non configurata: {name}")
        kind, value = target
        if kind == "uri":
            os.startfile(value)
        else:
            subprocess.Popen(value, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                             shell=False)
        return f"Apro {name}."

    @staticmethod
    def web_search(query: str) -> str:
        webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote_plus(query))
        return f"Cerco {query}."

    @staticmethod
    def world_map() -> str:
        webbrowser.open("https://argosatlas.com/")
        return "Apro Franco Mappa con la vista mondiale in tempo reale."


def build_runtime():
    from .actions import ActionRegistry
    from .runtime import FrancoRuntime

    local = WindowsActions()
    actions = ActionRegistry()
    actions.register("open_app", local.open_app)
    actions.register("web_search", local.web_search)
    actions.register("world_map", local.world_map)
    return FrancoRuntime(OpenRouterBrain(), actions)
