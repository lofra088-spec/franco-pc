"""franco.cyber.reporting sub-package (lazy re-exports)."""
import importlib

_EXPORTS = {
    "EvidenceManager": "evidence",
    "Exporter": "export",
    "ReportGenerator": "report",
}

__all__ = sorted(_EXPORTS)


def __getattr__(name):
    leaf = _EXPORTS.get(name)
    if leaf is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    mod = importlib.import_module(f"{__name__}.{leaf}")
    value = getattr(mod, name)
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(list(globals()) + __all__))
