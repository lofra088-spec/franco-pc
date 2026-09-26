"""franco.commands.web — Web.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).

Web commands are CommandEngine methods today. Extract the web/search handlers into this module next.
"""

from .._monolith import (
    CommandEngine,
)

__all__ = [
    "CommandEngine",
]
