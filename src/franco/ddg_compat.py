"""Small DuckDuckGo HTML adapter used by the merged Jarvis services."""
from __future__ import annotations
import html
import re
import urllib.parse
import urllib.request

def search_duckduckgo(query: str, limit: int = 8) -> list[dict[str, str]]:
    if not query.strip():
        raise ValueError("Inserisci una ricerca")
    body = urllib.request.urlopen(urllib.request.Request(
        "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": query}),
        headers={"User-Agent": "FRANCO-Jarvis/7.0"}), timeout=15).read().decode("utf-8", "replace")
    results = []
    for match in re.finditer(r'class="result__a" href="([^"]+)"[^>]*>(.*?)</a>', body, re.I | re.S):
        url = html.unescape(match.group(1)); title = re.sub(r"<[^>]+>", "", html.unescape(match.group(2))).strip()
        if url.startswith("//duckduckgo.com/l/?"):
            parsed = urllib.parse.parse_qs(urllib.parse.urlparse(url).query); url = parsed.get("uddg", [url])[0]
        results.append({"title": title, "url": url})
        if len(results) >= max(1, min(limit, 20)): break
    return results

__all__ = ["search_duckduckgo"]
