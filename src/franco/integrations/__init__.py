"""franco.integrations sub-package (lazy re-exports)."""
import importlib

_EXPORTS = {
    "EarthquakeMonitor": "earthquakes",
    "EmailConfigManager": "email",
    "HomeAssistantBridge": "home_assistant",
    "MobileBridge": "mobile",
    "ProactiveMonitor": "proactive",
    "PushNotifier": "notifications",
    "RemoteDeviceController": "remote",
    "JarvisBridge": "jarvis_bridge",
    "JarvisServices": "jarvis_services",
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
