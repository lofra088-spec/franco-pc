"""FRANCO 6.0 — NEXUS EDITION.

F.R.A.N.C.O. 6.0 — NEXUS EDITION
Full Responsive Autonomous Neural Control Operator.

Clean package over the historical monolith (src/franco/_monolith.py). Imports
are lazy (PEP 562): pulling one sub-module does not import its heavy siblings,
so light subsystems (e.g. franco.cyber) load without the whole app.
"""
__version__ = "6.0.0"
__codename__ = "NEXUS"

__all__ = ["__version__", "__codename__", "get_core"]


def get_core():
    """Lazily build and return the FrancoCore coordinator (loads the monolith)."""
    from .app import FrancoCore
    return FrancoCore()


