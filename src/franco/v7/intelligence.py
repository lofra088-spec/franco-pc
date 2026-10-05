"""Public-source intelligence helpers for Franco V7.

The module deliberately avoids people-data scraping. Person research returns
an attributable public-encyclopedia match and opens Max Intel for a manual,
authorized follow-up. It never aggregates home addresses, phone numbers,
private accounts, leaked credentials or inferred current locations.
"""
from __future__ import annotations

import base64
import json
import os
import re
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path
from typing import ClassVar


class IntelligenceError(RuntimeError):
    pass


class PublicIntelligence:
    MAX_IMAGE_BYTES = 15 * 1024 * 1024
    IMAGE_EXTENSIONS: ClassVar[set[str]] = {".jpg", ".jpeg", ".png", ".webp"}
    ARGOS_MAP = "https://www.argosatlas.com/map/"
    MAXINTEL_PERSON = "https://maxintel.org/person.html"
    GEOSPY_ENDPOINT = "https://dev.geospy.ai/predict_v1"

    def __init__(self, *, open_url=None, urlopen=None):
        self._open_url = open_url or webbrowser.open
        self._urlopen = urlopen or urllib.request.urlopen

    @staticmethod
    def _safe_person_name(name: str) -> str:
        value = " ".join(str(name or "").split()).strip(" .,-")
        if not 2 <= len(value) <= 100:
            raise IntelligenceError("Indica il nome della persona da cercare.")
        if ("@" in value or "http://" in value.casefold() or "https://" in value.casefold()
                or re.search(r"\d{5,}", value)):
            raise IntelligenceError(
                "La ricerca persone accetta un nome pubblico, non email, telefoni o indirizzi."
            )
        if not re.search(r"[A-Za-zÀ-ÖØ-öø-ÿ]", value):
            raise IntelligenceError("Il nome indicato non e' valido.")
        return value

    def research_person(self, name: str) -> str:
        """Return a sourced public-profile lead and open Max Intel's legal hub."""
        name = self._safe_person_name(name)
        self._open_url(self.MAXINTEL_PERSON)
        params = urllib.parse.urlencode({
            "action": "query", "format": "json", "generator": "search",
            "gsrsearch": name, "gsrnamespace": 0, "gsrlimit": 1,
            "prop": "extracts|info", "exintro": 1, "explaintext": 1,
            "inprop": "url", "redirects": 1, "utf8": 1,
        })
        url = "https://it.wikipedia.org/w/api.php?" + params
        try:
            data = self._get_json(url)
            pages = list((data.get("query") or {}).get("pages", {}).values())
        except (OSError, ValueError, TypeError):
            pages = []
        if not pages:
            return (
                f"Ho aperto Max Intel per la ricerca pubblica di {name}. "
                "Non ho trovato una corrispondenza enciclopedica affidabile: "
                "non invento identita' e non raccolgo contatti, indirizzi o dati privati."
            )
        page = pages[0]
        title = str(page.get("title") or name)
        extract = " ".join(str(page.get("extract") or "").split())[:1200]
        source = str(page.get("fullurl") or
                     "https://it.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")))
        if not extract:
            extract = "La fonte pubblica ha restituito il profilo, ma senza una sintesi testuale."
        return (
            f"Possibile corrispondenza pubblica: {title}. {extract}\n"
            f"Fonte verificabile: {source}\n"
            "Ho aperto anche Max Intel per il confronto manuale. Verifica sempre che si tratti "
            "della persona giusta; Franco esclude dati privati e sensibili."
        )

    def open_map(self, location: str, layer: str) -> str:
        location = " ".join(str(location or "").split()).strip(" .")
        if not location or len(location) > 160:
            raise IntelligenceError("Indica una citta' o una zona valida.")
        params = urllib.parse.urlencode({"q": location, "limit": 1, "lang": "it"})
        try:
            data = self._get_json("https://photon.komoot.io/api/?" + params)
            features = data.get("features") or []
            lon, lat = features[0]["geometry"]["coordinates"][:2]
            lon, lat = float(lon), float(lat)
            if not (-180 <= lon <= 180 and -90 <= lat <= 90):
                raise ValueError("coordinate fuori intervallo")
            target = f"{self.ARGOS_MAP}#view={lat:.6f},{lon:.6f},11"
        except (OSError, ValueError, TypeError, KeyError, IndexError):
            target = self.ARGOS_MAP
        self._open_url(target)
        label = "telecamere pubbliche" if layer == "telecamere" else "voli pubblici in tempo reale"
        return (f"Apro Franco Mappa centrata su {location} per mostrare {label}. "
                "I dati e le fonti restano quelli pubblicati da Argos Atlas.")

    def geolocate_image(self, image_path: str) -> str:
        path = Path(image_path).expanduser().resolve()
        if not path.is_file() or path.suffix.casefold() not in self.IMAGE_EXTENSIONS:
            raise IntelligenceError("Indica un file JPG, PNG o WebP esistente.")
        if path.stat().st_size > self.MAX_IMAGE_BYTES:
            raise IntelligenceError("L'immagine supera il limite di 15 MB.")
        key = os.getenv("GEOSPY_API_KEY", "").strip()
        if not key:
            self._open_url("https://geospy.ai/")
            return ("GeoSpy non e' configurato: ho aperto il sito ufficiale. "
                    "Per usarlo dentro Franco imposta GEOSPY_API_KEY; ogni risultato sara' "
                    "mostrato come stima, non come posizione certa.")
        payload = json.dumps({
            "image": base64.b64encode(path.read_bytes()).decode("ascii")
        }).encode("utf-8")
        request = urllib.request.Request(
            self.GEOSPY_ENDPOINT, data=payload, method="POST",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        )
        try:
            data = self._get_json(request, timeout=45)
        except (OSError, ValueError, TypeError) as exc:
            raise IntelligenceError(f"GeoSpy non ha risposto correttamente: {exc}") from exc
        guesses = self._location_guesses(data)
        if not guesses:
            return "GeoSpy non ha restituito una stima utilizzabile per questa immagine."
        lines = ["Stime GeoSpy, da verificare:"]
        for index, guess in enumerate(guesses[:3], 1):
            lines.append(f"{index}. {guess}")
        lines.append("La geolocalizzazione visiva puo' sbagliare: non trattare queste stime come prova.")
        return "\n".join(lines)

    def _get_json(self, target, *, timeout: int = 8):
        request = target
        if isinstance(target, str):
            request = urllib.request.Request(target, headers={"User-Agent": "FrancoV7/7.0"})
        with self._urlopen(request, timeout=timeout) as response:
            return json.load(response)

    @staticmethod
    def _location_guesses(data) -> list[str]:
        if isinstance(data, dict):
            candidates = (data.get("predictions") or data.get("locations")
                          or data.get("data") or data.get("result") or [])
            if isinstance(candidates, dict):
                candidates = [candidates]
        elif isinstance(data, list):
            candidates = data
        else:
            candidates = []
        output = []
        for item in candidates:
            if not isinstance(item, dict):
                continue
            parts = [item.get(key) for key in ("city", "region", "country") if item.get(key)]
            if not parts and item.get("location"):
                parts = [item["location"]]
            if parts:
                confidence = item.get("confidence") or item.get("score")
                suffix = f" (confidenza {confidence})" if confidence is not None else ""
                output.append(", ".join(map(str, parts)) + suffix)
        return output
