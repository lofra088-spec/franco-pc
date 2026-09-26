"""FRANCO Workspace: a local, dependency-free productivity dashboard."""

__all__ = ["serve"]


def serve(**kwargs):
    from .server import serve as run
    return run(**kwargs)
