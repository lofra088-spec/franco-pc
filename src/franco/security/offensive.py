"""franco.security.offensive — Offensive.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).
"""

from .._monolith import (
    AttackLab,
    OffensiveToolkit,
    render_hack_catalog,
)

__all__ = [
    "AttackLab",
    "OffensiveToolkit",
    "render_hack_catalog",
]
