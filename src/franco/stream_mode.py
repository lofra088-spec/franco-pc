"""Allowlisted streaming workspace launcher for Windows."""
from __future__ import annotations
import os
import subprocess
import webbrowser
from pathlib import Path

STREAM_URLS = (
    "https://dashboard.twitch.tv/",
    "https://www.google.com/",
)

def _launch_candidates(candidates: list[str]) -> bool:
    for candidate in candidates:
        path = Path(os.path.expandvars(candidate))
        try:
            if path.is_file():
                subprocess.Popen([str(path)], close_fds=True)
                return True
            subprocess.Popen([candidate], close_fds=True)
            return True
        except (OSError, FileNotFoundError):
            continue
    return False

def launch_stream_workspace() -> str:
    """Open OBS, Discord and the selected browser dashboards.

    Steam and Streamlabs are deliberately excluded from this workspace.
    """
    launched = []
    if _launch_candidates([r"%ProgramFiles%\obs-studio\bin\64bit\obs64.exe", r"%ProgramFiles(x86)%\obs-studio\bin\64bit\obs64.exe", "obs64.exe"]):
        launched.append("OBS")
    if _launch_candidates([r"%LocalAppData%\Discord\Update.exe", r"%ProgramFiles%\Discord\Discord.exe", "discord.exe"]):
        launched.append("Discord")
    browser = os.environ.get("FRANCO_BROWSER", "chrome")
    try:
        subprocess.Popen([browser, *STREAM_URLS], close_fds=True)
        launched.append("Chrome con Twitch e Google")
    except OSError:
        for url in STREAM_URLS:
            webbrowser.open_new_tab(url)
        launched.append("browser con Twitch e Google")
    return "Modalità Stream avviata: " + ", ".join(launched) + "."
