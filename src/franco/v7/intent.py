"""Deterministic intent recognition for commands that must feel instant."""
from __future__ import annotations

import re
import unicodedata

from .contracts import Intent


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.replace("’", "'")
    return re.sub(r"\s+", " ", text).strip()


class IntentParser:
    """Parses local actions first and leaves open conversation to the brain."""

    _OPEN = re.compile(r"^(?:ehi franco[, ]*)?(?:apri|avvia|lancia)\s+(.+)$", re.IGNORECASE)
    _SEARCH = re.compile(
        r"^(?:ehi franco[, ]*)?(?:cerca|cercami|trova|trovami|googla)"
        r"(?:\s+su google|\s+online|\s+sul web)?\s+(.+)$", re.IGNORECASE,
    )
    _DESKTOP = re.compile(
        r"^(?:franco code\s+)?(?:usa\s+)?computer use\s*(?:per|:|-)?\s*(.+)$", re.IGNORECASE,
    )
    _CAMERAS = re.compile(
        r"^(?:ehi franco[, ]*)?(?:mostra(?:mi)?|apri|fammi vedere)\s+"
        r"(?:tutte\s+)?(?:le\s+)?telecamere(?:\s+(?:di|a|su))?\s+(.+)$", re.IGNORECASE,
    )
    _FLIGHTS = re.compile(
        r"^(?:ehi franco[, ]*)?(?:mostra(?:mi)?|apri|fammi vedere)\s+"
        r"(?:tutti\s+)?(?:i\s+)?voli(?:\s+(?:di|a|su|sopra))?\s+(.+)$", re.IGNORECASE,
    )
    _PERSON = re.compile(
        r"^(?:ehi franco[, ]*)?(?:cerca|ricerca|trova|analizza)\s+"
        r"(?:informazioni\s+su\s+)?(?:una\s+)?persona(?:\s+(?:di nome|chiamata))?\s+(.+)$",
        re.IGNORECASE,
    )
    _GEOSPY = re.compile(
        r"^(?:ehi franco[, ]*)?(?:geolocalizza|localizza|trova dove e stata scattata)\s+"
        r"(?:questa\s+)?(?:foto|immagine)?\s*(.+)$", re.IGNORECASE,
    )
    _SELF_REF = ("nel tuo codice", "il tuo codice", "tuo codice", "te stesso",
                 "da solo", "auto-miglior", "automiglior", "migliora franco",
                 "migliora te", "migliorati", "sistemati", "aggiustati",
                 "risolvi questo bug", "correggi questo bug", "sistema questo bug")
    _SELF_VERB = ("risolvi", "correggi", "aggiusta", "sistema", "debugga",
                  "migliora", "ottimizza", "potenzia", "modifica", "ripara",
                  "fix", "patch")
    _REVERT = ("annulla l'ultimo miglioramento", "annulla ultimo miglioramento",
               "annulla il miglioramento", "ripristina il tuo codice",
               "ripristina il codice", "rollback miglioramento",
               "annulla modifica al codice")
    _SENSITIVE_DESKTOP = (
        "invia", "pubblica", "compra", "acquista", "cancella", "elimina",
        "carica", "upload", "stampa", "avvia live", "avvia trasmissione",
        "login", "accedi", "password", "paga", "bonifico",
    )

    def parse(self, text: str) -> Intent:
        clean = normalize(text)
        if not clean:
            return Intent("empty", confidence=1.0)
        lowered = clean.casefold()
        stripped = lowered.strip(" ,.!?")
        if stripped in {"conferma miglioramento", "applica miglioramento",
                        "conferma la modifica", "applica la modifica"}:
            return Intent("apply_improvement", confidence=1.0)
        if stripped in {"annulla miglioramento", "scarta miglioramento",
                        "annulla la modifica", "scarta la modifica"}:
            return Intent("cancel_improvement", confidence=1.0)
        if stripped in {"ferma computer use", "stop computer use",
                        "ferma controllo computer"}:
            return Intent("desktop_stop", confidence=1.0)
        if stripped in {"conferma computer use", "confermo computer use",
                        "conferma azione computer"}:
            return Intent("desktop_confirm", confidence=1.0)
        if stripped in {"stato computer use", "come va computer use",
                        "a che punto e computer use"}:
            return Intent("desktop_status", confidence=1.0)
        if stripped in self._REVERT:
            return Intent("revert_improve", confidence=1.0)
        if any(trigger in lowered for trigger in self._SELF_REF) and (
                any(verb in lowered for verb in self._SELF_VERB)
                or any(trigger in lowered for trigger in self._SELF_REF[:5])):
            return Intent("self_improve", {"problem": clean}, .95)
        if stripped in {
            "franco mappa", "apri franco mappa", "apri la mappa",
            "mostra la mappa del mondo", "mappa mondiale",
        }:
            return Intent("world_map", confidence=1.0)
        match = self._CAMERAS.match(clean)
        if match:
            return Intent("map_search", {"location": match.group(1).strip(" ."),
                                         "layer": "telecamere"}, .99)
        match = self._FLIGHTS.match(clean)
        if match:
            return Intent("map_search", {"location": match.group(1).strip(" ."),
                                         "layer": "voli"}, .99)
        match = self._PERSON.match(clean)
        if match:
            return Intent("person_research", {"name": match.group(1).strip(" .")}, .98)
        match = self._GEOSPY.match(clean)
        if match and match.group(1).strip(" ."):
            return Intent("image_geolocation", {"image_path": match.group(1).strip(" .\"")}, .96)
        match = self._DESKTOP.match(clean)
        if match:
            goal = match.group(1).strip()
            sensitive = any(word in goal.casefold() for word in self._SENSITIVE_DESKTOP)
            return Intent("desktop_goal", {"goal": goal}, .98,
                          requires_confirmation=sensitive)
        match = self._OPEN.match(clean)
        if match:
            return Intent("open_app", {"name": match.group(1).strip(" .")}, .99)
        match = self._SEARCH.match(clean)
        if match:
            return Intent("web_search", {"query": match.group(1).strip()}, .99)
        if stripped in {"conferma", "confermo", "conferma azione"}:
            return Intent("confirm", confidence=1.0)
        if stripped in {"annulla", "stop", "fermati", "annulla azione"}:
            return Intent("cancel", confidence=1.0)
        return Intent("conversation", {"text": clean}, .75)
