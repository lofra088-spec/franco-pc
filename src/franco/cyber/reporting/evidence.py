"""Evidence collection & chain of custody."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Optional

logger = logging.getLogger(__name__)


@dataclass
class EvidenceManagerResult:
    operation: str = "evidence"
    success: bool = False
    findings: list[dict] = field(default_factory=list)
    note: str = ""

    def as_dict(self) -> dict:
        return {
            "category": "evidence",
            "operation": self.operation,
            "success": self.success,
            "findings": self.findings,
            "note": self.note,
            "severity": "info",
        }


class EvidenceManager:
    """Evidence collection & chain of custody.

    Scaffold: importabile e con superficie-metodi cablata. Le tecniche vere si
    implementano qui in un passo successivo — nessuna funzionalita' simulata.
    """

    def __init__(self, data_dir: Optional[Any] = None) -> None:
        self.data_dir = data_dir

    async def run(self, target: str = "", **kw: Any) -> list[dict]:
        logger.info("EvidenceManager.run target=%s", target)
        return [EvidenceManagerResult(note="scaffold — implement evidence").as_dict()]

    async def collect(self, target: str = "", **kw: Any) -> list[dict]:
        return await self.run(target, **kw)


__all__ = ["EvidenceManager", "EvidenceManagerResult"]
