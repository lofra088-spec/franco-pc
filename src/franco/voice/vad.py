"""franco.voice.vad — Vad.

Public surface re-exported from the FRANCO monolith (src/franco/_monolith.py).

Voice-activity / wake-word detection currently lives inside VoiceRecognizer. Extract the VAD loop here next.
"""

from .._monolith import (
    VoiceRecognizer,
)

__all__ = [
    "VoiceRecognizer",
]
