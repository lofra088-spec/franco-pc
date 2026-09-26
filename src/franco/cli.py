"""Lightweight diagnostics and version flags, with legacy CLI compatibility."""
import argparse
import json
import sys

__all__ = ["main"]


def main():
    args = sys.argv[1:]
    if "--doctor" in args or "--capabilities" in args or "--version" in args:
        parser = argparse.ArgumentParser(description="Diagnostica FRANCO senza avviare servizi")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--doctor", action="store_true", help="Verifica ambiente e dipendenze")
        group.add_argument("--capabilities", action="store_true", help="Elenca le capacità disponibili")
        group.add_argument("--version", action="store_true", help="Mostra la versione")
        parser.add_argument("--json", action="store_true", help="Diagnostica in formato JSON")
        options = parser.parse_args(args)
        if options.version:
            if options.json:
                parser.error("--json richiede --doctor")
            from . import __version__, __codename__
            print(f"FRANCO {__version__} {__codename__}")
            return 0
        if options.capabilities:
            from .capabilities import capability_catalog
            report = capability_catalog()
            print(json.dumps(report, ensure_ascii=False, indent=2) if options.json else
                  "\n".join(f"[{('OK' if item['configured'] else 'CONFIGURA')}] {item['name']}" for item in report))
            return 0
        from .diagnostics import collect_diagnostics, format_report
        report = collect_diagnostics()
        print(json.dumps(report, ensure_ascii=False, indent=2) if options.json else format_report(report))
        return 1 if report["summary"]["error"] else 0
    from .app import main as run_application
    return run_application()
