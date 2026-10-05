"""Minimal console entry point for exercising V7 without the legacy runtime."""
from __future__ import annotations

import argparse

from .services import build_runtime


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="franco --v7", description="Franco V7 clean runtime")
    parser.add_argument("--once", metavar="TESTO", help="Esegue una sola richiesta")
    parser.add_argument("--desktop", action="store_true",
                        help="Apre la sfera arancione e l'interfaccia desktop")
    parser.add_argument("--self-improve", metavar="PROBLEMA",
                        help="Franco modifica il proprio codice per risolvere il problema")
    parser.add_argument("--revert-improve", action="store_true",
                        help="Annulla l'ultima auto-modifica del codice")
    args = parser.parse_args(argv)
    if args.desktop:
        from .desktop_ui import run_desktop
        return run_desktop(build_runtime())
    if args.self_improve is not None:
        from .self_improve import SelfImprover
        from .services import OpenRouterBrain
        print(SelfImprover(OpenRouterBrain()).prepare(args.self_improve))
        return 0
    if args.revert_improve:
        from .self_improve import SelfImprover
        from .services import OpenRouterBrain
        print(SelfImprover(OpenRouterBrain()).revert_last())
        return 0
    runtime = build_runtime()
    if args.once is not None:
        print(runtime.submit_final(args.once).text)
        return 0
    print("Franco V7 pronto. Scrivi 'esci' per terminare.")
    while True:
        try:
            text = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if text.casefold() in {"esci", "quit", "exit"}:
            return 0
        print(runtime.submit_final(text).text)
