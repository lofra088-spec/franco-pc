"""franco.ai.base — Base.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).

Abstract AI-client surface. Real base class is extracted here in a later pass; for now the Claude client is the reference.
"""

from .._monolith import (
    ClaudeAIClient,
)

__all__ = [
    "ClaudeAIClient",
]
