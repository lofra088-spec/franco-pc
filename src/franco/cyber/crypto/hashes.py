"""Hash identification and dictionary cracking."""

from __future__ import annotations

import asyncio
import hashlib
import logging
import re
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# regex fingerprints -> candidate algorithms (by length/charset)
_HASH_SHAPES: list[tuple[str, str, list[str]]] = [
    (r"^[a-f0-9]{32}$", "32hex", ["md5", "ntlm"]),
    (r"^[a-f0-9]{40}$", "40hex", ["sha1"]),
    (r"^[a-f0-9]{56}$", "56hex", ["sha224"]),
    (r"^[a-f0-9]{64}$", "64hex", ["sha256"]),
    (r"^[a-f0-9]{96}$", "96hex", ["sha384"]),
    (r"^[a-f0-9]{128}$", "128hex", ["sha512"]),
    (r"^\$2[aby]\$\d\d\$", "bcrypt", ["bcrypt"]),
    (r"^\$6\$", "sha512crypt", ["sha512crypt"]),
    (r"^\$1\$", "md5crypt", ["md5crypt"]),
]

# algorithms crackable with a plain hashlib comparison
_HASHLIB = {
    "md5": "md5", "sha1": "sha1", "sha224": "sha224",
    "sha256": "sha256", "sha384": "sha384", "sha512": "sha512",
}

_COMMON = [
    "123456", "password", "123456789", "12345678", "qwerty", "abc123",
    "111111", "123123", "admin", "letmein", "welcome", "monkey",
    "dragon", "iloveyou", "root", "toor", "pass", "test",
]


class HashCracker:
    """Identifica e cracka hash via dizionario."""

    def __init__(self, data_dir: Optional[Path] = None) -> None:
        self.data_dir = Path(data_dir) if data_dir else None

    def identify(self, value: str) -> list[str]:
        """Ritorna le algoritmo-candidate per la forma dell'hash."""
        v = value.strip().lower()
        for pattern, _label, algos in _HASH_SHAPES:
            if re.match(pattern, v):
                return algos
        return []

    async def crack(self, hash_value: str, hash_type: str = "auto",
                    wordlist: str = "") -> dict:
        """Cracka via dizionario. Ritorna {'cracked', 'plaintext', ...}."""
        value = hash_value.strip().lower()
        candidates = ([hash_type] if hash_type and hash_type != "auto"
                      else self.identify(value))
        usable = [c for c in candidates if c in _HASHLIB]

        if not usable:
            return {"category": "hash", "cracked": False, "hash": hash_value,
                    "identified_as": candidates,
                    "note": "algoritmo non crackabile con hashlib (es. bcrypt) — usa hashcat"}

        words = await self._load_words(wordlist)
        loop = asyncio.get_event_loop()
        plaintext = await loop.run_in_executor(
            None, self._brute, value, usable, words)

        if plaintext is not None:
            return {"category": "hash", "cracked": True, "hash": hash_value,
                    "plaintext": plaintext, "algorithm": usable,
                    "severity": "high", "tried": len(words)}
        return {"category": "hash", "cracked": False, "hash": hash_value,
                "identified_as": candidates, "severity": "info", "tried": len(words)}

    def _brute(self, target: str, algos: list[str], words: list[str]) -> Optional[str]:
        for word in words:
            wb = word.encode("utf-8", "ignore")
            for algo in algos:
                if hashlib.new(_HASHLIB[algo], wb).hexdigest() == target:
                    return word
        return None

    async def _load_words(self, wordlist: str) -> list[str]:
        path = None
        if wordlist:
            path = Path(wordlist)
        elif self.data_dir:
            default = self.data_dir / "wordlists" / "passwords.txt"
            if default.exists():
                path = default
        if path and path.exists():
            try:
                return [w.strip() for w in
                        path.read_text(encoding="utf-8", errors="ignore").splitlines()
                        if w.strip()]
            except Exception as exc:  # noqa: BLE001
                logger.warning("wordlist load failed: %s", exc)
        return list(_COMMON)
