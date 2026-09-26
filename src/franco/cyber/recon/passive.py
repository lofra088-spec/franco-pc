"""Passive reconnaissance — OSINT."""

from __future__ import annotations

import asyncio
import json
import logging
import socket
import urllib.parse
from dataclasses import dataclass
from typing import Any, Optional

logger = logging.getLogger(__name__)


@dataclass
class PassiveResult:
    category: str
    data: Any
    severity: str = "info"


class PassiveRecon:
    """Ricognizione passiva OSINT."""

    def __init__(self, data_dir) -> None:
        self.data_dir = data_dir

    async def run_all(self, target: str) -> list[dict]:
        """Esegui tutte le tecniche passive."""
        results = []

        tasks = [
            self.dns_enum(target),
            self.whois_lookup(target),
            self.reverse_dns(target),
            self.subdomain_enum(target),
            self.google_dorks(target),
            self.shodan_lookup(target),
            self.certificate_transparency(target),
            self.social_profiles(target),
        ]

        for task in tasks:
            try:
                task_results = await task
                results.extend(task_results)
            except Exception as e:
                logger.warning("Passive recon error: %s", e)

        return results

    async def dns_enum(self, target: str) -> list[dict]:
        """Enumerazione DNS."""
        results = []
        record_types = ["A", "AAAA", "MX", "NS", "TXT", "SOA", "CNAME"]

        for rtype in record_types:
            try:
                loop = asyncio.get_event_loop()
                answers = await loop.run_in_executor(
                    None, lambda: socket.getaddrinfo(target, None, socket.AF_INET)
                )
                if answers:
                    ips = list(set(a[4][0] for a in answers))
                    results.append({
                        "category": "dns",
                        "type": rtype,
                        "target": target,
                        "values": ips,
                        "severity": "info"
                    })
            except Exception:
                pass

        return results

    async def whois_lookup(self, target: str) -> list[dict]:
        """Whois lookup."""
        try:
            import pythonwhois
            loop = asyncio.get_event_loop()
            whois_data = await loop.run_in_executor(
                None, pythonwhois.get_whois, target
            )
            return [{
                "category": "whois",
                "target": target,
                "data": {k: str(v) for k, v in whois_data.items() if v},
                "severity": "info"
            }]
        except ImportError:
            logger.warning("pythonwhois not installed")
            return []
        except Exception as e:
            logger.warning("Whois failed: %s", e)
            return []

    async def reverse_dns(self, ip: str) -> list[dict]:
        """Reverse DNS lookup."""
        try:
            loop = asyncio.get_event_loop()
            hostname = await loop.run_in_executor(
                None, socket.gethostbyaddr, ip
            )
            return [{
                "category": "reverse_dns",
                "ip": ip,
                "hostname": hostname[0],
                "aliases": hostname[1],
                "severity": "info"
            }]
        except Exception:
            return []

    async def subdomain_enum(self, target: str) -> list[dict]:
        """Enumerazione subdomini via certificate transparency."""
        subdomains = set()

        # CRT.sh query
        try:
            import aiohttp
            domain = target.replace("http://", "").replace("https://", "").split("/")[0]
            url = f"https://crt.sh/?q=%.{domain}&output=json"

            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        for entry in data:
                            name = entry.get("name_value", "")
                            for sub in name.split("\n"):
                                sub = sub.strip("*.")
                                if sub and sub != domain:
                                    subdomains.add(sub)
        except Exception as e:
            logger.warning("CRT.sh query failed: %s", e)

        # Wordlist-based (se disponibile)
        wordlist_path = self.data_dir / "wordlists" / "subdomains.txt"
        if wordlist_path.exists():
            for sub in wordlist_path.read_text().splitlines():
                sub = sub.strip()
                if sub:
                    full = f"{sub}.{target}"
                    try:
                        socket.gethostbyname(full)
                        subdomains.add(full)
                    except socket.gaierror:
                        pass

        return [{
            "category": "subdomains",
            "target": target,
            "subdomains": sorted(subdomains),
            "count": len(subdomains),
            "severity": "info"
        }]

    async def google_dorks(self, target: str) -> list[dict]:
        """Google dorks per information disclosure."""
        dorks = [
            f"site:{target} filetype:pdf",
            f"site:{target} filetype:xlsx",
            f"site:{target} filetype:docx",
            f"site:{target} inurl:admin",
            f"site:{target} inurl:login",
            f"site:{target} inurl:.env",
            f"site:{target} \"password\" filetype:log",
            f"site:{target} intitle:\"index of\"",
        ]

        results = []
        for dork in dorks:
            results.append({
                "category": "google_dork",
                "dork": dork,
                "note": "Run manually or via scraping API",
                "severity": "low"
            })

        return results

    async def shodan_lookup(self, target: str) -> list[dict]:
        """Shodan information gathering."""
        api_key = __import__("os").environ.get("SHODAN_API_KEY")
        if not api_key:
            return [{"category": "shodan", "note": "SHODAN_API_KEY not set", "severity": "info"}]

        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.shodan.io/shodan/host/{target}?key={api_key}",
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return [{
                            "category": "shodan",
                            "target": target,
                            "ports": data.get("ports", []),
                            "vulns": data.get("vulns", []),
                            "hostnames": data.get("hostnames", []),
                            "org": data.get("org", ""),
                            "os": data.get("os", ""),
                            "severity": "medium" if data.get("vulns") else "info"
                        }]
        except Exception as e:
            logger.warning("Shodan failed: %s", e)

        return []

    async def certificate_transparency(self, target: str) -> list[dict]:
        """Certificate transparency logs."""
        # Già coperto in subdomain_enum via crt.sh
        return []

    async def social_profiles(self, target: str) -> list[dict]:
        """Cerca profili social associati."""
        platforms = [
            "github.com", "gitlab.com", "twitter.com", "linkedin.com",
            "reddit.com", "hackerone.com", "bugcrowd.com"
        ]

        found = []
        domain = target.replace("http://", "").replace("https://", "").split("/")[0]
        org_name = domain.split(".")[0]

        for platform in platforms:
            found.append({
                "category": "social",
                "platform": platform,
                "possible_url": f"https://{platform}/{org_name}",
                "note": "Verify manually",
                "severity": "info"
            })

        return found
