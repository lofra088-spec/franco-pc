"""Strict validation at the API and database boundaries."""
from copy import deepcopy
from datetime import date, datetime
import re
from urllib.parse import urlsplit

from .errors import WorkspaceError


def validate_field(value, spec):
    kind = spec["type"]
    if value is None:
        if spec["required"] or spec["default"] is not None:
            raise ValueError("Campo obbligatorio")
        return None
    if kind == "boolean":
        if type(value) is not bool:
            raise ValueError("Deve essere vero o falso")
        return value
    if kind in ("integer", "money"):
        if type(value) is not int:
            raise ValueError("Deve essere un numero intero" if kind == "integer" else "L'importo deve essere espresso in centesimi interi")
        if value < spec.get("minimum", value):
            raise ValueError(f'Minimo: {spec["minimum"]}')
        if value > spec.get("maximum", value):
            raise ValueError(f'Massimo: {spec["maximum"]}')
        return value
    if kind == "tags":
        if not isinstance(value, list) or len(value) > 20:
            raise ValueError("Usa una lista di massimo 20 tag")
        result = []
        for tag in value:
            if not isinstance(tag, str) or not tag.strip() or len(tag) > 50:
                raise ValueError("Ogni tag deve contenere da 1 a 50 caratteri")
            tag = tag.strip()
            if tag not in result:
                result.append(tag)
        return result
    if not isinstance(value, str):
        raise ValueError("Deve essere un testo")
    if "\x00" in value:
        raise ValueError("Il testo contiene un carattere non valido")
    if kind not in ("multiline", "code"):
        value = value.strip()
    if spec["required"] and not value.strip():
        raise ValueError("Campo obbligatorio")
    if len(value) > spec["max_length"]:
        raise ValueError(f'Massimo {spec["max_length"]} caratteri')
    if kind == "select" and value not in spec["options"]:
        raise ValueError("Scegli un valore disponibile")
    if kind in ("date", "datetime", "reference") and not value:
        return None
    if kind == "date":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError("Usa una data nel formato AAAA-MM-GG")
        date.fromisoformat(value)
    if kind == "datetime":
        # A local agenda uses wall-clock times, without ambiguous mixed offsets.
        parsed = datetime.fromisoformat(value)
        if "T" not in value or parsed.tzinfo is not None:
            raise ValueError("Usa data e ora locali, senza fuso orario")
        value = parsed.isoformat(timespec="minutes")
    if kind == "url" and value:
        try:
            parts = urlsplit(value)
            valid = parts.scheme in ("http", "https") and parts.hostname and not parts.username and not parts.password
            _ = parts.port
        except ValueError:
            valid = False
        if not valid or any(ch.isspace() or ord(ch) < 32 for ch in value):
            raise ValueError("Inserisci un indirizzo http o https valido, senza credenziali")
    if kind == "email" and value:
        if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", value):
            raise ValueError("Inserisci un indirizzo email valido")
    if kind == "reference":
        if not re.fullmatch(r"[0-9a-f]{32}", value):
            raise ValueError("Riferimento non valido")
    return value


def validate_record(payload, fields, *, partial=False):
    if not isinstance(payload, dict):
        raise WorkspaceError("Invia un oggetto JSON")
    unknown = set(payload) - set(fields)
    if unknown:
        raise WorkspaceError("Campi sconosciuti", fields={key: "Campo non ammesso" for key in sorted(unknown)})
    result = {}
    errors = {}
    for name, spec in fields.items():
        if partial and name not in payload:
            continue
        value = payload.get(name, deepcopy(spec["default"]))
        try:
            result[name] = validate_field(value, spec)
        except (ValueError, OverflowError) as exc:
            errors[name] = str(exc)
    if errors:
        raise WorkspaceError("Controlla i campi evidenziati", fields=errors)
    return result


def validate_consistency(resource, record):
    if resource == "events" and record["end_at"] < record["start_at"]:
        raise WorkspaceError("La fine precede l'inizio", fields={"end_at": "Scegli un orario successivo all'inizio"})


def positive_int(value, name, *, default=1, maximum=1000000):
    if value is None:
        return default
    if isinstance(value, bool):
        raise WorkspaceError(f"{name}: valore non valido")
    try:
        parsed = int(value)
    except (TypeError, ValueError, OverflowError):
        raise WorkspaceError(f"{name}: inserisci un intero positivo") from None
    if str(parsed) != str(value) or not 1 <= parsed <= maximum:
        raise WorkspaceError(f"{name}: usa un valore tra 1 e {maximum}")
    return parsed
