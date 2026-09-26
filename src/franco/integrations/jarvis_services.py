"""Jarvis services that were missing from the original FRANCO runtime.

All network calls have short timeouts and return plain serializable data. The
module intentionally keeps credentials out of URLs except for services that
require them, and shell execution is explicit and opt-in.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any


def _get_json(url: str, timeout: float = 12) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": "FRANCO-Jarvis/7.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


class JarvisServices:
    """Weather, maps, news, stocks, calendar and web features from Jarvis."""

    def weather(self, latitude: float, longitude: float, timezone: str = "auto") -> dict[str, Any]:
        query = urllib.parse.urlencode({"latitude": latitude, "longitude": longitude,
                                        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
                                        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
                                        "timezone": timezone})
        return _get_json("https://api.open-meteo.com/v1/forecast?" + query)

    def geocode(self, query: str, limit: int = 5) -> list[dict[str, Any]]:
        if not query.strip():
            raise ValueError("Inserisci una località")
        params = urllib.parse.urlencode({"q": query, "format": "jsonv2", "limit": max(1, min(limit, 10))})
        return _get_json("https://nominatim.openstreetmap.org/search?" + params)

    def route(self, start: tuple[float, float], end: tuple[float, float]) -> dict[str, Any]:
        a, b = start, end
        url = f"https://router.project-osrm.org/route/v1/driving/{a[1]},{a[0]};{b[1]},{b[0]}?overview=false&steps=true"
        return _get_json(url)

    def stock(self, symbol: str) -> dict[str, Any]:
        symbol = symbol.strip().upper()
        if not re.fullmatch(r"[A-Z0-9.\-]{1,15}", symbol):
            raise ValueError("Simbolo azionario non valido")
        # Stooq is free and needs no account for the latest quote.
        rows = urllib.request.urlopen(
            urllib.request.Request(f"https://stooq.com/q/l/?s={urllib.parse.quote(symbol)}&f=sd2t2ohlcv&h&e=json",
                                   headers={"User-Agent": "FRANCO-Jarvis/7.0"}), timeout=12)
        return json.load(rows)

    def news(self, feed_url: str = "https://feeds.bbci.co.uk/news/world/rss.xml", limit: int = 10) -> list[dict[str, str]]:
        raw = urllib.request.urlopen(urllib.request.Request(feed_url, headers={"User-Agent": "FRANCO-Jarvis/7.0"}), timeout=12).read()
        root = ET.fromstring(raw)
        items = []
        for item in root.findall(".//item")[: max(1, min(limit, 30))]:
            items.append({"title": (item.findtext("title") or "").strip(),
                          "url": (item.findtext("link") or "").strip(),
                          "published": (item.findtext("pubDate") or "").strip(),
                          "summary": (item.findtext("description") or "").strip()})
        return items

    def calendar_ics(self, url: str) -> list[dict[str, str]]:
        """Read a remote iCalendar feed without storing its contents."""
        if not url.lower().startswith(("https://", "http://")):
            raise ValueError("Il calendario deve usare HTTP(S)")
        text = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "FRANCO-Jarvis/7.0"}), timeout=15).read(2_000_000).decode("utf-8", "replace")
        events, current = [], None
        for line in text.replace("\r\n ", "").splitlines():
            if line == "BEGIN:VEVENT": current = {}
            elif line == "END:VEVENT" and current is not None:
                events.append(current); current = None
            elif current is not None and ":" in line:
                key, value = line.split(":", 1); current[key.split(";", 1)[0]] = value
        return [{"title": e.get("SUMMARY", ""), "start": e.get("DTSTART", ""), "end": e.get("DTEND", ""), "location": e.get("LOCATION", "")} for e in events]

    def web_search(self, query: str, limit: int = 8) -> list[dict[str, str]]:
        from ..ddg_compat import search_duckduckgo
        return search_duckduckgo(query, limit=limit)

    def run_shell(self, command: str, timeout: int = 30) -> dict[str, Any]:
        if os.getenv("FRANCO_ALLOW_SHELL", "").lower() not in {"1", "true", "yes"}:
            return {"error": "Shell disabilitata. Imposta FRANCO_ALLOW_SHELL=1 per abilitarla esplicitamente."}
        if not command.strip() or len(command) > 4000:
            raise ValueError("Comando non valido")
        completed = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=max(1, min(timeout, 120)))
        return {"returncode": completed.returncode, "stdout": completed.stdout[-12000:], "stderr": completed.stderr[-12000:]}


__all__ = ["JarvisServices"]
