"""Web application scanner — tech detection + baseline vuln checks."""

from __future__ import annotations

import asyncio
import logging
import re
import ssl
import urllib.request
from typing import Optional

logger = logging.getLogger(__name__)

# response-header / body fingerprints -> technology label
_TECH_SIGNS = {
    "server": {"nginx": "nginx", "apache": "Apache", "iis": "IIS",
               "cloudflare": "Cloudflare", "gunicorn": "Gunicorn"},
    "x-powered-by": {"php": "PHP", "asp.net": "ASP.NET", "express": "Express"},
    "body": {"wp-content": "WordPress", "drupal": "Drupal",
             "joomla": "Joomla", "__NEXT_DATA__": "Next.js",
             "ng-version": "Angular", "data-reactroot": "React"},
}

# security headers a good site should send
_SECURITY_HEADERS = [
    "content-security-policy", "strict-transport-security",
    "x-frame-options", "x-content-type-options", "referrer-policy",
]


class WebScanner:
    """Scanner web non intrusivo (GET + analisi header/corpo)."""

    def __init__(self, timeout: float = 10.0, user_agent: str = "") -> None:
        self.timeout = timeout
        self.user_agent = user_agent or "FRANCO-CyberScanner/1.0"

    async def _fetch(self, url: str) -> tuple[int, dict, str]:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._fetch_sync, url)

    def _fetch_sync(self, url: str) -> tuple[int, dict, str]:
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        req = urllib.request.Request(url, headers={"User-Agent": self.user_agent})
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(req, timeout=self.timeout, context=ctx) as resp:
            body = resp.read(200_000).decode("utf-8", "replace")
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return resp.status, headers, body

    async def detect_tech(self, url: str) -> list[dict]:
        """Rileva stack tecnologico da header e corpo."""
        try:
            status, headers, body = await self._fetch(url)
        except Exception as exc:  # noqa: BLE001
            return [{"category": "web_tech", "url": url,
                     "error": str(exc), "severity": "info"}]

        found = []
        for header, table in _TECH_SIGNS.items():
            haystack = body.lower() if header == "body" else headers.get(header, "").lower()
            for needle, label in table.items():
                if needle in haystack:
                    found.append({"category": "web_tech", "url": url,
                                  "technology": label, "via": header,
                                  "severity": "info"})
        if not found:
            found.append({"category": "web_tech", "url": url,
                          "technology": "unknown", "status": status,
                          "severity": "info"})
        return found

    async def scan(self, url: str) -> list[dict]:
        """Controlli baseline: header di sicurezza mancanti, cookie, banner."""
        try:
            status, headers, body = await self._fetch(url)
        except Exception as exc:  # noqa: BLE001
            return [{"category": "web_vuln", "url": url,
                     "error": str(exc), "severity": "info"}]

        findings = []
        for h in _SECURITY_HEADERS:
            if h not in headers:
                findings.append({
                    "category": "web_vuln", "url": url,
                    "issue": f"missing security header: {h}",
                    "severity": "low",
                })

        # cookie senza flag
        cookie = headers.get("set-cookie", "")
        if cookie:
            low = cookie.lower()
            if "httponly" not in low:
                findings.append({"category": "web_vuln", "url": url,
                                 "issue": "cookie without HttpOnly", "severity": "medium"})
            if "secure" not in low:
                findings.append({"category": "web_vuln", "url": url,
                                 "issue": "cookie without Secure", "severity": "medium"})

        # server banner verboso
        server = headers.get("server", "")
        if re.search(r"\d+\.\d+", server):
            findings.append({"category": "web_vuln", "url": url,
                             "issue": f"verbose server banner: {server}",
                             "severity": "low"})
        return findings
