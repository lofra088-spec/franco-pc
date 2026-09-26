"""Encoding / decoding multi-tool."""

from __future__ import annotations

import base64
import binascii
import codecs
import html
import urllib.parse
from typing import Union

Bytes = Union[str, bytes]


def _b(data: Bytes) -> bytes:
    return data.encode() if isinstance(data, str) else data


class Encoder:
    """Encode/decode per le rappresentazioni più comuni in security work."""

    # ── base64 ──────────────────────────────────────────────────────────
    def b64_encode(self, data: Bytes) -> str:
        return base64.b64encode(_b(data)).decode()

    def b64_decode(self, data: str) -> bytes:
        return base64.b64decode(data + "=" * (-len(data) % 4))

    def b64url_encode(self, data: Bytes) -> str:
        return base64.urlsafe_b64encode(_b(data)).decode().rstrip("=")

    def b64url_decode(self, data: str) -> bytes:
        return base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))

    # ── hex ─────────────────────────────────────────────────────────────
    def hex_encode(self, data: Bytes) -> str:
        return _b(data).hex()

    def hex_decode(self, data: str) -> bytes:
        return bytes.fromhex(data.replace(" ", "").replace("0x", ""))

    # ── url ─────────────────────────────────────────────────────────────
    def url_encode(self, data: str) -> str:
        return urllib.parse.quote(data, safe="")

    def url_decode(self, data: str) -> str:
        return urllib.parse.unquote(data)

    # ── html ────────────────────────────────────────────────────────────
    def html_encode(self, data: str) -> str:
        return html.escape(data)

    def html_decode(self, data: str) -> str:
        return html.unescape(data)

    # ── rot13 / caesar ──────────────────────────────────────────────────
    def rot13(self, data: str) -> str:
        return codecs.encode(data, "rot_13")

    def caesar(self, data: str, shift: int) -> str:
        out = []
        for ch in data:
            if ch.isalpha():
                base = ord("A") if ch.isupper() else ord("a")
                out.append(chr((ord(ch) - base + shift) % 26 + base))
            else:
                out.append(ch)
        return "".join(out)

    # ── xor ─────────────────────────────────────────────────────────────
    def xor(self, data: Bytes, key: Bytes) -> bytes:
        d, k = _b(data), _b(key)
        return bytes(b ^ k[i % len(k)] for i, b in enumerate(d))

    # ── binary ──────────────────────────────────────────────────────────
    def to_binary(self, data: Bytes) -> str:
        return " ".join(f"{byte:08b}" for byte in _b(data))

    def from_binary(self, bits: str) -> bytes:
        cleaned = bits.replace(" ", "")
        return bytes(int(cleaned[i:i + 8], 2) for i in range(0, len(cleaned), 8))

    # ── auto-decode chain ───────────────────────────────────────────────
    def try_all(self, data: str) -> dict[str, str]:
        """Prova le decodifiche comuni e ritorna quelle che riescono."""
        out: dict[str, str] = {}
        attempts = {
            "base64": lambda: self.b64_decode(data).decode("utf-8", "replace"),
            "base64url": lambda: self.b64url_decode(data).decode("utf-8", "replace"),
            "hex": lambda: self.hex_decode(data).decode("utf-8", "replace"),
            "url": lambda: self.url_decode(data),
            "html": lambda: self.html_decode(data),
            "rot13": lambda: self.rot13(data),
        }
        for name, fn in attempts.items():
            try:
                result = fn()
                if result and result != data:
                    out[name] = result
            except (ValueError, binascii.Error, UnicodeDecodeError):
                pass
        return out
