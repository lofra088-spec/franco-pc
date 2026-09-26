"""Spotify desktop adapter without storing credentials.

Search is handed to the installed Spotify client through its URI protocol;
playback controls use Windows media keys. Account sign-in remains in Spotify.
"""
from __future__ import annotations

import ctypes
import re
import urllib.parse
import webbrowser


class SpotifyAdapter:
    VK_MEDIA_NEXT_TRACK = 0xB0
    VK_MEDIA_PREV_TRACK = 0xB1
    VK_MEDIA_PLAY_PAUSE = 0xB3
    KEYUP = 0x0002

    @staticmethod
    def _media_key(code):
        user32 = ctypes.windll.user32
        user32.keybd_event(code, 0, 0, 0)
        user32.keybd_event(code, 0, SpotifyAdapter.KEYUP, 0)

    def handle(self, command):
        text = str(command).strip()
        low = text.lower()
        if "spotify" not in low:
            return None
        if any(word in low for word in ("pausa", "riprendi", "play", "metti in pausa")):
            self._media_key(self.VK_MEDIA_PLAY_PAUSE)
            return "Comando riproduzione inviato a Spotify."
        if any(word in low for word in ("prossima", "prossimo", "cambia brano", "salta")):
            self._media_key(self.VK_MEDIA_NEXT_TRACK)
            return "Passo al prossimo brano su Spotify."
        if any(word in low for word in ("precedente", "indietro")):
            self._media_key(self.VK_MEDIA_PREV_TRACK)
            return "Torno al brano precedente su Spotify."
        match = re.search(r"(?:cerca|riproduci|metti)\s+(.+?)(?:\s+su spotify)?$", text,
                          flags=re.IGNORECASE)
        if match:
            query = match.group(1).strip()
            webbrowser.open("spotify:search:" + urllib.parse.quote(query))
            return f"Ho aperto la ricerca di {query} su Spotify."
        if any(word in low for word in ("apri", "avvia")):
            webbrowser.open("spotify:")
            return "Apro Spotify. L'accesso resta gestito in modo sicuro dall'app Spotify."
        return ("Puoi dirmi: cerca su Spotify, pausa Spotify, prossimo brano Spotify "
                "oppure apri Spotify.")
