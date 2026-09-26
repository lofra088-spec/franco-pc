"""System hardening checks (read-only audit)."""

from __future__ import annotations

import logging
import os
import platform
import subprocess
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Check:
    name: str
    passed: bool
    severity: str
    detail: str

    def as_finding(self) -> dict:
        return {
            "category": "hardening",
            "check": self.name,
            "state": "pass" if self.passed else "fail",
            "severity": "info" if self.passed else self.severity,
            "detail": self.detail,
        }


class SystemHardener:
    """Audit di hardening — non modifica nulla, solo diagnosi.

    Le raccomandazioni di remediation sono stringhe: applicarle è una scelta
    esplicita dell'operatore, mai automatica.
    """

    def __init__(self) -> None:
        self.system = platform.system()

    async def run_all(self) -> list[dict]:
        checks = [
            self._check_admin(),
            self._check_firewall(),
            self._check_updates_hint(),
            self._check_open_shares_hint(),
        ]
        return [c.as_finding() for c in checks]

    def _check_admin(self) -> Check:
        """Il processo gira con privilegi elevati?"""
        elevated = False
        try:
            if self.system == "Windows":
                import ctypes
                elevated = bool(ctypes.windll.shell32.IsUserAnAdmin())
            else:
                elevated = hasattr(os, "geteuid") and os.geteuid() == 0
        except Exception as exc:  # noqa: BLE001
            return Check("privilege_level", True, "info", f"non determinabile: {exc}")
        return Check(
            "privilege_level", not elevated, "medium",
            "in esecuzione con privilegi elevati (riduci la superficie)"
            if elevated else "privilegi utente standard",
        )

    def _check_firewall(self) -> Check:
        """Stato firewall (best-effort per OS)."""
        try:
            if self.system == "Windows":
                out = subprocess.run(
                    ["netsh", "advfirewall", "show", "allprofiles", "state"],
                    capture_output=True, text=True, timeout=10,
                ).stdout.lower()
                on = "on" in out and "off" not in out.replace("state", "")
                return Check("firewall", on, "high",
                             "profili firewall attivi" if "on" in out
                             else "firewall disattivato su uno o più profili")
            if self.system == "Linux":
                out = subprocess.run(["which", "ufw"], capture_output=True,
                                     text=True, timeout=5).stdout.strip()
                return Check("firewall", bool(out), "high",
                             "ufw presente" if out else "nessun ufw rilevato")
        except Exception as exc:  # noqa: BLE001
            return Check("firewall", True, "info", f"stato non determinabile: {exc}")
        return Check("firewall", True, "info", "controllo non supportato su questo OS")

    def _check_updates_hint(self) -> Check:
        return Check("updates", True, "info",
                     "verifica manuale aggiornamenti di sistema consigliata")

    def _check_open_shares_hint(self) -> Check:
        return Check("network_shares", True, "info",
                     "verifica condivisioni SMB/NFS esposte")
