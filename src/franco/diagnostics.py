"""Read-only startup diagnostics. No application imports or network requests."""
from importlib.util import find_spec
import os
from pathlib import Path
import platform
import sys
from .capabilities import capability_catalog

__all__ = ["collect_diagnostics", "format_report"]


def collect_diagnostics():
    checks = []
    def check(name, ok, detail, required=False):
        checks.append(dict(name=name, status="ok" if ok else "error" if required else "warning", detail=detail))

    check("Python", sys.version_info >= (3, 10), f"{platform.python_version()} — {sys.executable}", True)
    legacy = Path(os.environ.get("FRANCO_LEGACY_HOME", Path(__file__).resolve().parents[3]))
    check("Moduli locali", (legacy / "francov6reall.py").is_file(), str(legacy))
    modules = {
        "dotenv": ("Configurazione .env", "python-dotenv"),
        "requests": ("Connessioni HTTP", "requests"),
        "anthropic": ("Claude", "anthropic"),
        "speech_recognition": ("Riconoscimento vocale", "SpeechRecognition"),
        "pyaudio": ("Microfono", "pyaudio"),
        "pygame": ("Interfaccia e audio", "pygame"),
        "PIL": ("Immagini", "Pillow"),
        "psutil": ("Metriche di sistema", "psutil"),
        "numpy": ("Elaborazione audio", "numpy"),
        "cryptography": ("Archivio cifrato", "cryptography"),
    }
    for module, (label, distribution) in modules.items():
        try:
            available = find_spec(module) is not None
        except (ImportError, ValueError, AttributeError):
            available = False
        check(label, available, f"Modulo disponibile: {distribution}" if available else f"Installazione: python -m pip install {distribution}")
    env_paths = [legacy / ".env", Path(__file__).resolve().parents[2] / ".env", Path(__file__).parent / ".env"]
    check("File .env", any(p.is_file() for p in env_paths), "File presente; contenuto non visualizzato" if any(p.is_file() for p in env_paths) else "Facoltativo: puoi usare le variabili d'ambiente")
    for capability in capability_catalog():
        check("Capacità " + capability["name"], capability["configured"],
              "Configurata" if capability["configured"] else "Configurazione facoltativa mancante")
    return {"checks": checks, "summary": {status: sum(c["status"] == status for c in checks) for status in ("ok", "warning", "error")}}


def format_report(report):
    lines = ["FRANCO — Diagnostica locale", "Verifica disponibilità moduli; non prova microfono, credenziali o servizi.", ""]
    labels = {"ok": "OK", "warning": "AVVISO", "error": "ERRORE"}
    for item in report["checks"]:
        lines.append(f'[{labels[item["status"]]}] {item["name"]}: {item["detail"]}')
    counts = report["summary"]
    lines.append(f'\n{counts["ok"]} OK, {counts["warning"]} avvisi, {counts["error"]} errori.')
    return "\n".join(lines)
