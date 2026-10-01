"""Minimal console entry point for exercising V7 without the legacy runtime."""
from __future__ import annotations

import argparse

from .services import build_runtime


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="franco --v7", description="Franco V7 clean runtime")
    parser.add_argument("--once", metavar="TESTO", help="Esegue una sola richiesta")
    args = parser.parse_args(argv)
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

