"""franco.commands.files — Files.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).

File commands are CommandEngine methods today. Extract the file-op handlers into this module next.
"""

from .._monolith import (
    CommandEngine,
)

__all__ = [
    "CommandEngine",
]
