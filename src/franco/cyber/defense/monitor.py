"""Real-time network monitoring."""

from __future__ import annotations

import asyncio
import logging
import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, AsyncIterator, Optional

logger = logging.getLogger(__name__)


@dataclass
class Connection:
    src_ip: str
    src_port: int
    dst_ip: str
    dst_port: int
    protocol: str
    state: str
    bytes_sent: int = 0
    bytes_recv: int = 0
    timestamp: float = field(default_factory=time.time)


@dataclass
class Alert:
    type: str
    severity: str
    description: str
    data: dict[str, Any]
    timestamp: float = field(default_factory=time.time)


class NetworkMonitor:
    """Monitoraggio rete in tempo reale."""

    def __init__(self) -> None:
        self._connections: dict[str, Connection] = {}
        self._alerts: list[Alert] = []
        self._stats = defaultdict(lambda: {"count": 0, "bytes": 0})
        self._suspicious_ports = {4444, 5555, 6666, 7777, 8888, 9999,
                                  31337, 12345, 54321, 65535}
        self._blocked_ips: set[str] = set()

    async def stream(self, interface: str = "") -> AsyncIterator[dict]:
        """Stream eventi rete — da usare con scapy o tcpdump."""

        try:
            from scapy.all import sniff, IP, TCP, UDP, conf
            conf.verb = 0

            def packet_callback(pkt):
                if not pkt.haslayer(IP):
                    return None

                src = pkt[IP].src
                dst = pkt[IP].dst
                proto = pkt[IP].proto

                sport = dport = 0
                if pkt.haslayer(TCP):
                    sport = pkt[TCP].sport
                    dport = pkt[TCP].dport
                    proto = "TCP"
                elif pkt.haslayer(UDP):
                    sport = pkt[UDP].sport
                    dport = pkt[UDP].dport
                    proto = "UDP"

                # Check suspicious
                return self._analyze(src, sport, dst, dport, proto)

            queue: asyncio.Queue = asyncio.Queue()
            loop = asyncio.get_event_loop()

            def async_callback(pkt):
                result = packet_callback(pkt)
                if result:
                    asyncio.run_coroutine_threadsafe(queue.put(result), loop)

            sniff_thread = loop.run_in_executor(
                None, lambda: sniff(prn=async_callback, store=0,
                                    iface=interface or None)
            )
            _ = sniff_thread  # fire-and-forget sniffer

            while True:
                event = await queue.get()
                yield event

        except ImportError:
            logger.warning("scapy not installed — using psutil fallback")
            async for event in self._psutil_monitor():
                yield event

    async def _psutil_monitor(self) -> AsyncIterator[dict]:
        """Fallback monitor con psutil."""
        try:
            import psutil
            seen = set()

            while True:
                try:
                    conn = psutil.net_connections(kind='inet')
                    for c in conn:
                        if c.status == 'ESTABLISHED':
                            raddr = c.raddr if c.raddr else None
                            key = (f"{c.laddr.ip}:{c.laddr.port}->"
                                   f"{raddr.ip if raddr else ''}:{raddr.port if raddr else 0}")
                            if key not in seen:
                                seen.add(key)

                                event = self._analyze(
                                    c.laddr.ip, c.laddr.port,
                                    raddr.ip if raddr else "",
                                    raddr.port if raddr else 0,
                                    "TCP"
                                )
                                if event:
                                    yield event
                except (psutil.AccessDenied, PermissionError):
                    pass

                await asyncio.sleep(2)

        except ImportError:
            logger.error("Neither scapy nor psutil available")

    def _analyze(self, src_ip: str, src_port: int,
                 dst_ip: str, dst_port: int,
                 protocol: str) -> Optional[dict]:
        """Analizza connessione per anomalie."""

        alerts = []

        # Reverse shell ports
        if dst_port in self._suspicious_ports or src_port in self._suspicious_ports:
            alerts.append({
                "type": "suspicious",
                "severity": "high",
                "description": f"Suspicious port: {dst_port}",
                "src": f"{src_ip}:{src_port}",
                "dst": f"{dst_ip}:{dst_port}",
            })

        # Known C2 ports
        c2_ports = {4444, 5555, 1337, 31337, 4443}
        if dst_port in c2_ports and dst_ip not in self._blocked_ips:
            alerts.append({
                "type": "suspicious",
                "severity": "critical",
                "description": f"Possible C2 connection to port {dst_port}",
                "src": f"{src_ip}:{src_port}",
                "dst": f"{dst_ip}:{dst_port}",
            })

        # Outbound to unusual ports
        if dst_port > 49152 and src_ip.startswith(("192.168.", "10.", "172.")):
            alerts.append({
                "type": "unusual_outbound",
                "severity": "medium",
                "description": f"Outbound to high port {dst_port}",
                "src": f"{src_ip}:{src_port}",
                "dst": f"{dst_ip}:{dst_port}",
            })

        if alerts:
            return alerts[0]
        return None
