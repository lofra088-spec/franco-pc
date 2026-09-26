"""Single capability catalog shared by diagnostics, UI and Jarvis bridge."""
from __future__ import annotations

CAPABILITIES = (
    ("openrouter", "Chat OpenRouter", "OPENROUTER_API_KEY"),
    ("xtts", "Voce locale XTTS", "FRANCO_XTTS_PYTHON"),
    ("weather", "Meteo Open-Meteo", None),
    ("maps", "Geocoding e percorsi OpenStreetMap", None),
    ("news", "Notizie RSS", None),
    ("stocks", "Quotazioni Stooq", None),
    ("calendar", "Calendari iCal", None),
    ("web_search", "Ricerca DuckDuckGo", None),
    ("home_assistant", "Home Assistant", "HOME_ASSISTANT_URL"),
    ("mobile", "Bridge mobile", "FRANCO_MOBILE_API_KEY"),
    ("jarvis_client", "Client Jarvis/HUD", None),
)

def capability_catalog(env=None):
    import os
    if env is None:
        env = dict(os.environ)
        # Diagnostics are also useful before the full app bootstrap. Read the
        # project .env here so the report reflects the real installation.
        try:
            from dotenv import dotenv_values
            root = __import__("pathlib").Path(__file__).resolve().parents[2]
            for key, value in dotenv_values(root / ".env").items():
                if value and not env.get(key):
                    env[key] = value
        except Exception:
            pass
    if env.get("FRANCO_XTTS_URL") or env.get("FRANCO_XTTS_PYTHON"):
        env = dict(env)
        env["FRANCO_XTTS_PYTHON"] = env.get("FRANCO_XTTS_PYTHON") or env.get("FRANCO_XTTS_URL")
    return [{"id": key, "name": name, "configured": bool(env.get(variable)) if variable else True}
            for key, name, variable in CAPABILITIES]

__all__ = ["CAPABILITIES", "capability_catalog"]
