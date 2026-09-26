"""Web content/parameter fuzzer."""

from __future__ import annotations

import asyncio
import logging
import ssl
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# small built-in path list; a real run points at a wordlist file
_DEFAULT_PATHS = [
    "admin", "administrator", "login", "wp-admin", "wp-login.php",
    ".git/HEAD", ".env", "config.php", "backup", "backup.zip",
    "robots.txt", "sitemap.xml", "api", "api/v1", "phpinfo.php",
    "server-status", ".htaccess", "debug", "test", "old",
]

# interesting statuses to report
_REPORT = {200, 201, 204, 301, 302, 401, 403, 500}


class WebFuzzer:
    """Fuzzing di path via wordlist (concorrenza limitata)."""

    def __init__(self, timeout: float = 6.0, concurrency: int = 20,
                 user_agent: str = "") -> None:
        self.timeout = timeout
        self._sem = asyncio.Semaphore(concurrency)
        self.user_agent = user_agent or "FRANCO-CyberFuzzer/1.0"

    def _paths(self, wordlist: str = "") -> list[str]:
        if wordlist:
            p = Path(wordlist)
            if p.exists():
                return [w.strip() for w in
                        p.read_text(encoding="utf-8", errors="ignore").splitlines()
                        if w.strip() and not w.startswith("#")]
        return list(_DEFAULT_PATHS)

    async def run(self, url: str, wordlist: str = "") -> list[dict]:
        """Fuzza i path e ritorna quelli con status interessanti."""
        base = url if url.startswith(("http://", "https://")) else "http://" + url
        base = base.rstrip("/")
        tasks = [self._probe(f"{base}/{path}", path) for path in self._paths(wordlist)]
        findings = []
        for fut in asyncio.as_completed(tasks):
            res = await fut
            if res:
                findings.append(res)
        findings.sort(key=lambda f: f["path"])
        return findings

    async def _probe(self, full_url: str, path: str) -> Optional[dict]:
        async with self._sem:
            loop = asyncio.get_event_loop()
            try:
                status = await loop.run_in_executor(None, self._head, full_url)
            except Exception:
                return None
        if status in _REPORT:
            severity = "medium" if status in (200, 401, 403) else "low"
            if any(s in path for s in (".git", ".env", "backup", "config", "phpinfo")):
                severity = "high"
            return {"category": "web_fuzz", "url": full_url, "path": path,
                    "status": status, "severity": severity}
        return None

    def _head(self, url: str) -> int:
        req = urllib.request.Request(url, method="GET",
                                     headers={"User-Agent": self.user_agent})
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        try:
            with urllib.request.urlopen(req, timeout=self.timeout, context=ctx) as resp:
                return resp.status
        except urllib.error.HTTPError as exc:
            return exc.code
