"""Intrusion Detection System."""

from __future__ import annotations

import json
import logging
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)


@dataclass
class Rule:
    id: str
    name: str
    severity: str
    pattern: str
    category: str
    description: str = ""
    action: str = "alert"  # alert, block, log


class IntrusionDetector:
    """IDS base con regole custom."""

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir
        self.rules: list[Rule] = []
        self._load_default_rules()

        self.alerts: list[dict] = []
        self._stats = defaultdict(int)

    def _load_default_rules(self) -> None:
        """Carica regole predefinite."""
        default_rules = [
            Rule("ID1001", "SQL Injection Detection", "high",
                 r"(?i)(union\s+select|or\s+1\s*=\s*1|'\s*or\s*'|--\s*$|;\s*drop\s)",
                 "web", "Detects common SQL injection patterns"),

            Rule("ID1002", "XSS Detection", "medium",
                 r"(?i)<script[^>]*>|javascript:|on\w+\s*=",
                 "web", "Detects XSS attack patterns"),

            Rule("ID1003", "Path Traversal", "high",
                 r"\.\.[\\/]|%2e%2e[%/\\]|%252e%252e",
                 "web", "Detects path traversal attempts"),

            Rule("ID1004", "Command Injection", "critical",
                 r"(?i)(;\s*|\|\s*|&&\s*)(cat|ls|whoami|id|uname|wget|curl|nc|bash|sh)\b",
                 "web", "Detects OS command injection"),

            Rule("ID1005", "Log4j Detection", "critical",
                 r"\$\{jndi:(?:ldap|rmi|dns|nis|iiop|corba|nds|nis):",
                 "web", "Detects Log4Shell exploitation attempts"),

            Rule("ID1006", "SSRF Detection", "high",
                 r"(?i)(169\.254\.169\.254|metadata\.google|127\.0\.0\.1|localhost|0\.0\.0\.0)",
                 "web", "Detects SSRF to internal resources"),

            Rule("ID1007", "Brute Force Detection", "medium",
                 r"(?i)(failed\s+login|authentication\s+failed|invalid\s+(password|credential))",
                 "auth", "Detects brute force attempts"),

            Rule("ID1008", "Suspicious User Agent", "low",
                 r"(?i)(nikto|sqlmap|nmap|masscan|dirbuster|gobuster|wfuzz|hydra|metasploit)",
                 "recon", "Detects known attack tools"),

            Rule("ID1009", "Shellshock Detection", "critical",
                 r"\(\)\s*\{[^}]*\}\s*;",
                 "web", "Detects Shellshock exploitation"),

            Rule("ID1010", "PHP Injection", "high",
                 r"(?i)(<\?php|eval\s*\(|base64_decode|system\s*\(|exec\s*\(|passthru\s*\()",
                 "web", "Detects PHP code injection"),
        ]

        self.rules = default_rules

        # Load custom rules from file
        rules_file = self.data_dir / "ids_rules.json"
        if rules_file.exists():
            try:
                custom = json.loads(rules_file.read_text())
                for r in custom:
                    self.rules.append(Rule(**r))
            except Exception as e:
                logger.warning("Failed to load custom rules: %s", e)

    def check(self, data: str, source: str = "unknown") -> list[dict]:
        """Controlla dati contro le regole."""
        alerts = []

        for rule in self.rules:
            if re.search(rule.pattern, data):
                alert = {
                    "rule_id": rule.id,
                    "rule_name": rule.name,
                    "severity": rule.severity,
                    "category": rule.category,
                    "source": source,
                    "matched_pattern": rule.pattern,
                    "action": rule.action,
                }
                alerts.append(alert)
                self.alerts.append(alert)
                self._stats[rule.category] += 1

        return alerts

    def check_http_request(self, method: str, path: str,
                           headers: dict, body: str = "") -> list[dict]:
        """Controlla HTTP request."""
        data = f"{method} {path}\n"
        data += "\n".join(f"{k}: {v}" for k, v in headers.items())
        data += f"\n\n{body}"

        return self.check(data, source="http_request")

    def check_log_line(self, line: str) -> list[dict]:
        """Controlla riga di log."""
        return self.check(line, source="log")

    def add_rule(self, rule: Rule) -> None:
        """Aggiungi regola custom."""
        self.rules.append(rule)

    def get_stats(self) -> dict:
        """Statistiche allerta."""
        return {
            "total_alerts": len(self.alerts),
            "by_category": dict(self._stats),
            "by_severity": self._count_by_severity(),
        }

    def _count_by_severity(self) -> dict[str, int]:
        counts = defaultdict(int)
        for a in self.alerts:
            counts[a["severity"]] += 1
        return dict(counts)
