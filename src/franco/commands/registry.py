"""franco.commands.registry — Registry.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).
"""

from .._monolith import (
    CommandEngine,
    highlight_voice_command,
    render_voice_command_catalog,
)

__all__ = [
    "CommandEngine",
    "highlight_voice_command",
    "render_voice_command_catalog",
]
