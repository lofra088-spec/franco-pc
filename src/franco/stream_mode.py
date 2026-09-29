"""Allowlisted streaming workspace launcher for Windows."""
from __future__ import annotations
import os
import subprocess
import webbrowser

STREAM_URLS = (
    "https://dashboard.twitch.tv/",
    "https://www.google.com/",
)

def launch_stream_workspace() -> str:
    """Open OBS, Discord and the selected browser dashboards.

    Steam and Streamlabs are deliberately excluded from this workspace.
    """
    launched = []
    for executable, label in (("obs64", "OBS"), ("discord", "Discord")):
        try:
            subprocess.Popen([executable], close_fds=True)
            launched.append(label)
        except OSError:
            continue
    browser = os.environ.get("FRANCO_BROWSER", "chrome")
    try:
        subprocess.Popen([browser, *STREAM_URLS], close_fds=True)
        launched.append("Chrome con Twitch e Google")
    except OSError:
        for url in STREAM_URLS:
            webbrowser.open_new_tab(url)
        launched.append("browser con Twitch e Google")
    return "Modalità Stream avviata: " + ", ".join(launched) + "."

