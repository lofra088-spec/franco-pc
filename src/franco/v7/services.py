"""Dependency-light adapters used by the clean V7 runtime."""
from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
import webbrowser

from .app_launcher import WindowsAppLauncher
from .intelligence import PublicIntelligence


class OpenRouterBrain:
    """Small OpenAI-compatible client; no SDK is loaded into RAM."""

    endpoint = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.api_key = (api_key or os.getenv("OPENROUTER_API_KEY", "")).strip()
        self.model = model or os.getenv("FRANCO_OPENROUTER_MODEL", "openrouter/auto")

    def answer(self, text: str, *, context: list[dict[str, str]]) -> str:
        system = {
            "role": "system",
            "content": (
                "Sei Franco 7, assistente operativo personale. Rispondi in italiano naturale, "
                "breve e concreto. Interpreta con buon senso gli errori di trascrizione. "
                "Non dichiarare mai di avere eseguito un'azione se non ricevi un esito reale."
            ),
        }
        return self._chat([system, *context, {"role": "user", "content": text}],
                          temperature=.35, max_tokens=600)

    def complete(self, prompt: str, *, system: str, max_tokens: int = 2000,
                 temperature: float = .2, model: str | None = None) -> str:
        """Single-shot completion for code and self-modification tasks."""
        messages = [{"role": "system", "content": system},
                    {"role": "user", "content": prompt}]
        return self._chat(messages, temperature=temperature,
                          max_tokens=max_tokens, model=model)

    def _chat(self, messages: list[dict[str, str]], *, temperature: float,
              max_tokens: int, model: str | None = None) -> str:
        if not self.api_key:
            raise RuntimeError("OPENROUTER_API_KEY non configurata")
        payload = json.dumps({
            "model": model or self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }).encode("utf-8")
        request = urllib.request.Request(
            self.endpoint, data=payload, method="POST",
            headers={"Authorization": f"Bearer {self.api_key}",
                     "Content-Type": "application/json", "X-Title": "Franco 7"},
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            data = json.load(response)
        if not isinstance(data, dict) or not data.get("choices"):
            detail = data.get("error") if isinstance(data, dict) else None
            raise RuntimeError(f"Risposta OpenRouter non valida{': ' + str(detail) if detail else ''}")
        try:
            return str(data["choices"][0]["message"].get("content") or "").strip()
        except (KeyError, TypeError, IndexError) as exc:
            raise RuntimeError("OpenRouter non ha restituito testo utilizzabile") from exc


class WindowsActions:
    """Fast local actions without loading the legacy application."""

    def __init__(self):
        self._launcher = WindowsAppLauncher()

    def open_app(self, name: str) -> str:
        launched = self._launcher.launch(name)
        return f"Apro {launched}."

    @staticmethod
    def web_search(query: str) -> str:
        webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote_plus(query))
        return f"Cerco {query}."

    @staticmethod
    def world_map() -> str:
        webbrowser.open("https://www.argosatlas.com/map/")
        return "Apro Franco Mappa con la vista mondiale in tempo reale."


def build_runtime():
    from .actions import ActionRegistry
    from .runtime import FrancoRuntime
    from .self_improve import SelfImprover

    brain = OpenRouterBrain()
    local = WindowsActions()
    intelligence = PublicIntelligence()
    actions = ActionRegistry()
    actions.register("open_app", local.open_app)
    actions.register("web_search", local.web_search)
    actions.register("world_map", local.world_map)
    actions.register("map_search", intelligence.open_map)
    actions.register("person_research", intelligence.research_person)
    actions.register("image_geolocation", intelligence.geolocate_image)
    improver = SelfImprover(brain)
    actions.register("self_improve", improver.prepare)
    actions.register("apply_improvement", improver.apply_pending)
    actions.register("cancel_improvement", improver.cancel_pending)
    actions.register("revert_improve", improver.revert_last)
    return FrancoRuntime(brain, actions)
