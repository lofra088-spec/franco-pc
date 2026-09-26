"""JARVIS Cybersecurity Coordinator."""

from __future__ import annotations

import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from pathlib import Path
from typing import Any, Optional

from franco.core.events import EventBus, Event, Priority
from franco.core.exceptions import SecurityError

logger = logging.getLogger(__name__)


class OpMode(Enum):
    """Modalità operativa."""
    RECON = auto()
    OFFENSE = auto()
    DEFENSE = auto()
    ANALYSIS = auto()
    STEALTH = auto()


class TargetType(Enum):
    HOST = "host"
    NETWORK = "network"
    WEBAPP = "webapp"
    CODE = "code"
    MALWARE = "malware"


@dataclass
class Target:
    """Target per operazione."""
    type: TargetType
    value: str
    metadata: dict[str, Any] = field(default_factory=dict)
    notes: str = ""


@dataclass
class OpResult:
    """Risultato operazione."""
    success: bool
    operation: str
    findings: list[dict] = field(default_factory=list)
    raw_output: str = ""
    timestamp: datetime = field(default_factory=datetime.now)
    severity: str = "info"  # info, low, medium, high, critical


class CyberJarvis:
    """JARVIS Cybersecurity Module."""

    def __init__(self, events: EventBus, data_dir: Path) -> None:
        self.events = events
        self.data_dir = data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.mode = OpMode.RECON
        self.current_target: Optional[Target] = None
        self.operation_log: list[OpResult] = []

        # Lazy-loaded modules
        self._recon = None
        self._offense = None
        self._defense = None
        self._crypto = None
        self._websec = None
        self._malware = None

    # ── Module Access ───────────────────────────────────────────────────

    @property
    def recon(self):
        if self._recon is None:
            from franco.cyber.recon.passive import PassiveRecon
            from franco.cyber.recon.active import ActiveRecon
            self._recon = {"passive": PassiveRecon(self.data_dir),
                           "active": ActiveRecon(self.data_dir)}
        return self._recon

    @property
    def offense(self):
        if self._offense is None:
            from franco.cyber.offense.exploit import ExploitEngine
            from franco.cyber.offense.payload import PayloadGen
            from franco.cyber.offense.shells import ShellHandler
            self._offense = {"exploit": ExploitEngine(self.data_dir),
                             "payload": PayloadGen(self.data_dir),
                             "shells": ShellHandler()}
        return self._offense

    @property
    def defense(self):
        if self._defense is None:
            from franco.cyber.defense.monitor import NetworkMonitor
            from franco.cyber.defense.ids import IntrusionDetector
            from franco.cyber.defense.hardening import SystemHardener
            self._defense = {"monitor": NetworkMonitor(),
                             "ids": IntrusionDetector(self.data_dir),
                             "harden": SystemHardener()}
        return self._defense

    @property
    def crypto(self):
        if self._crypto is None:
            from franco.cyber.crypto.hashes import HashCracker
            from franco.cyber.crypto.encoding import Encoder
            self._crypto = {"hash": HashCracker(self.data_dir),
                            "encode": Encoder()}
        return self._crypto

    @property
    def websec(self):
        if self._websec is None:
            from franco.cyber.websec.scanner import WebScanner
            from franco.cyber.websec.fuzzer import WebFuzzer
            self._websec = {"scanner": WebScanner(),
                            "fuzzer": WebFuzzer()}
        return self._websec

    # ── High-Level Operations ───────────────────────────────────────────

    async def full_recon(self, target: str) -> OpResult:
        """Ricognizione completa di un target."""
        self.current_target = Target(type=TargetType.HOST, value=target)
        self.mode = OpMode.RECON

        findings = []

        # Phase 1: Passive
        await self.events.emit(Event("cyber.recon.passive.start", target=target))

        passive_results = await self.recon["passive"].run_all(target)
        findings.extend(passive_results)

        await self.events.emit(Event("cyber.recon.passive.done",
                                     findings=len(passive_results)))

        # Phase 2: Active
        await self.events.emit(Event("cyber.recon.active.start", target=target))

        active_results = await self.recon["active"].scan(target)
        findings.extend(active_results)

        await self.events.emit(Event("cyber.recon.active.done",
                                     findings=len(active_results)))

        result = OpResult(
            success=True,
            operation="full_recon",
            findings=findings,
        )
        self.operation_log.append(result)
        return result

    async def attack_surface(self, target: str) -> OpResult:
        """Mappa la superficie d'attacco."""
        findings = []

        # Port scan
        ports = await self.recon["active"].port_scan(target)
        findings.extend(ports)

        # Per ogni porta aperta, determina servizio e cerca vuln
        for port_info in [f for f in ports if f.get("state") == "open"]:
            service = port_info.get("service", "")
            _port = port_info.get("port", 0)

            # Cerca CVE noti per il servizio
            cves = await self._search_cve(service, port_info.get("version", ""))
            if cves:
                findings.extend(cves)

        result = OpResult(
            success=True,
            operation="attack_surface",
            findings=findings,
            severity=self._max_severity(findings)
        )
        self.operation_log.append(result)
        return result

    async def web_assessment(self, url: str) -> OpResult:
        """Assessment completo web application."""
        self.current_target = Target(type=TargetType.WEBAPP, value=url)

        findings = []

        # Tech detection
        tech = await self.websec["scanner"].detect_tech(url)
        findings.extend(tech)

        # Vulnerability scan
        vulns = await self.websec["scanner"].scan(url)
        findings.extend(vulns)

        # Fuzzing parametri
        fuzz_results = await self.websec["fuzzer"].run(url)
        findings.extend(fuzz_results)

        result = OpResult(
            success=True,
            operation="web_assessment",
            findings=findings,
            severity=self._max_severity(findings)
        )
        self.operation_log.append(result)
        return result

    async def exploit_target(self, target: str, exploit_id: str = "") -> OpResult:
        """Esegui exploit su target."""
        self.mode = OpMode.OFFENSE

        raw = await self.offense["exploit"].run(target, exploit_id)
        result = OpResult(
            success=raw.get("success", False),
            operation="exploit_target",
            findings=[raw],
            severity="high" if raw.get("success") else "info",
        )
        self.operation_log.append(result)
        return result

    async def generate_shell(self, lhost: str, lport: int,
                             shell_type: str = "reverse",
                             format: str = "python") -> OpResult:
        """Genera shell payload."""
        payload = self.offense["shells"].generate(
            shell_type=shell_type,
            lhost=lhost, lport=lport,
            fmt=format
        )

        return OpResult(
            success=True,
            operation="generate_shell",
            findings=[{"payload": payload, "type": shell_type, "format": format}]
        )

    async def crack_hash(self, hash_value: str, hash_type: str = "auto",
                         wordlist: str = "") -> OpResult:
        """Crack un hash."""
        result = await self.crypto["hash"].crack(hash_value, hash_type, wordlist)
        return OpResult(
            success=result.get("cracked", False),
            operation="crack_hash",
            findings=[result]
        )

    async def start_monitoring(self, interface: str = "") -> None:
        """Avvia monitoraggio rete in background."""
        await self.events.emit(Event("cyber.monitor.start", interface=interface))

        async for event in self.defense["monitor"].stream(interface):
            if event.get("type") == "suspicious" or event.get("severity") in ("high", "critical"):
                await self.events.emit(Event(
                    "cyber.alert",
                    data=event,
                    priority=Priority.HIGH
                ))

    async def harden_system(self) -> OpResult:
        """Hardening sistema."""
        findings = await self.defense["harden"].run_all()
        return OpResult(
            success=True,
            operation="harden_system",
            findings=findings
        )

    # ── Helpers ─────────────────────────────────────────────────────────

    async def _search_cve(self, service: str, version: str) -> list[dict]:
        """Cerca CVE per servizio/versione."""
        # Query locale DB o API esterna
        return []

    def _max_severity(self, findings: list[dict]) -> str:
        """Trova severità massima nei findings."""
        severity_order = ["info", "low", "medium", "high", "critical"]
        max_sev = "info"
        for f in findings:
            sev = f.get("severity", "info")
            if sev in severity_order and severity_order.index(sev) > severity_order.index(max_sev):
                max_sev = sev
        return max_sev

    def get_summary(self) -> dict:
        """Riassunto operazioni."""
        return {
            "mode": self.mode.name,
            "target": self.current_target.value if self.current_target else None,
            "total_operations": len(self.operation_log),
            "total_findings": sum(len(r.findings) for r in self.operation_log),
            "critical_findings": sum(
                1 for r in self.operation_log
                for f in r.findings
                if f.get("severity") == "critical"
            ),
        }
