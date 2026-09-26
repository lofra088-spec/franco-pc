"""franco.ai.router — Router.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).

Dual-AI router lives in franco_patch_dual_ai (optional). Facade holds the seam.
"""

from .._monolith import (
    ClaudeAIClient,
)

__all__ = [
    "ClaudeAIClient",
]
