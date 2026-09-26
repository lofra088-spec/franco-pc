"""franco.ai.mistral — Mistral.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).

Mistral client lives in franco_patch_dual_ai (optional). Facade re-exports the primary client until it is vendored.
"""

from .._monolith import (
    ClaudeAIClient,
)

__all__ = [
    "ClaudeAIClient",
]
