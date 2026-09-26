"""franco.app — App.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).

Central coordinator (FrancoCore) and CLI entrypoint (main).
"""

from ._monolith import (
    FrancoCore,
    main,
    parse_args,
)

__all__ = [
    "FrancoCore",
    "main",
    "parse_args",
]
