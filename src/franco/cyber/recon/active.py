"""Active reconnaissance — scanning."""

from __future__ import annotations

import asyncio
import logging
import socket
import struct
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
    1433: "MSSQL", 1521: "Oracle", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 5900: "VNC", 6379: "Redis", 8080: "HTTP-Alt",
    8443: "HTTPS-Alt", 27017: "MongoDB",
}


class ActiveRecon:
    """Ricognizione attiva."""

    def __init__(self, data_dir) -> None:
        self.data_dir = data_dir
        self._semaphore = asyncio.Semaphore(500)

    async def scan(self, target: str) -> list[dict]:
        """Scan completo."""
        results = []

        # Port scan
        ports = await self.port_scan(target)
        results.extend(ports)

        # Service detection su porte aperte
        open_ports = [p["port"] for p in ports if p["state"] == "open"]
        if open_ports:
            services = await self.service_detect(target, open_ports)
            results.extend(services)

        # OS fingerprint (base)
        os_info = await self.os_fingerprint(target)
        if os_info:
            results.append(os_info)

        return results

    async def port_scan(self, target: str,
                        ports: Optional[list[int]] = None,
                        timeout: float = 1.0) -> list[dict]:
        """Port scan con connect."""
        if ports is None:
            ports = list(COMMON_PORTS.keys())

        results = []
        tasks = [self._scan_port(target, port, timeout) for port in ports]

        for future in asyncio.as_completed(tasks):
            try:
                result = await future
                if result:
                    results.append(result)
            except Exception:
                pass

        # Sort by port number
        results.sort(key=lambda x: x["port"])
        return results

    async def _scan_port(self, host: str, port: int, timeout: float) -> Optional[dict]:
        """Scan singola porta."""
        async with self._semaphore:
            try:
                loop = asyncio.get_event_loop()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)

                result = await loop.run_in_executor(
                    None, sock.connect_ex, (host, port)
                )
                sock.close()

                if result == 0:
                    service = COMMON_PORTS.get(port, "unknown")
                    return {
                        "category": "port",
                        "port": port,
                        "state": "open",
                        "service": service,
                        "severity": "info"
                    }
            except Exception:
                pass
        return None

    async def service_detect(self, host: str, ports: list[int]) -> list[dict]:
        """Detect versione servizio con banner grabbing."""
        results = []

        for port in ports:
            try:
                loop = asyncio.get_event_loop()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)

                await loop.run_in_executor(None, sock.connect, (host, port))

                # Invia probe
                probes = {
                    80: b"HEAD / HTTP/1.0\r\nHost: " + host.encode() + b"\r\n\r\n",
                    443: b"\x16\x03\x01\x00\x05\x01\x00\x00\x01\x00",
                    21: b"\r\n",
                    25: b"EHLO probe\r\n",
                    110: b"\r\n",
                }

                probe = probes.get(port, b"")
                if probe:
                    await loop.run_in_executor(None, sock.send, probe)

                banner = await loop.run_in_executor(None, sock.recv, 1024)
                sock.close()

                if banner:
                    banner_str = banner.decode("utf-8", errors="replace").strip()
                    version = self._parse_version(banner_str)

                    results.append({
                        "category": "service",
                        "port": port,
                        "banner": banner_str[:200],
                        "detected_version": version,
                        "severity": "medium" if version else "info"
                    })
            except Exception:
                pass

        return results

    def _parse_version(self, banner: str) -> str:
        """Estrai versione dal banner."""
        import re
        patterns = [
            r"SSH-[\d.]+-OpenSSH[_\d.]+",
            r"Apache/[\d.]+",
            r"nginx/[\d.]+",
            r"Microsoft-IIS/[\d.]+",
            r"FTP server \(Version [\d.]+\)",
            r"MySQL [\d.]+",
            r"PostgreSQL [\d.]+",
            r"redis_version:[\d.]+",
        ]

        for pattern in patterns:
            match = re.search(pattern, banner, re.IGNORECASE)
            if match:
                return match.group(0)
        return ""

    async def os_fingerprint(self, host: str) -> Optional[dict]:
        """OS fingerprint base via TTL."""
        try:
            import os
            # getuid esiste solo su POSIX; su Windows salta (serve raw socket root)
            if not hasattr(os, "getuid") or os.getuid() != 0:
                return None

            # Simplified — in produzione usa scapy
            return None
        except Exception:
            return None
