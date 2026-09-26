"""Smoke test: every public import path resolves."""
import importlib

import pytest

MODULES = [
    "franco",
    "franco.app",
    "franco.core.exceptions", "franco.core.types", "franco.core.models",
    "franco.core.config", "franco.core.events", "franco.core.cache",
    "franco.core.state", "franco.core.logging", "franco.core.database",
    "franco.core.memory", "franco.core.backup", "franco.core.scheduler",
    "franco.core.utils",
    "franco.ai.claude", "franco.ai.nlp", "franco.ai.base",
    "franco.ai.mistral", "franco.ai.router",
    "franco.voice.stt", "franco.voice.tts", "franco.voice.vad",
    "franco.commands.registry", "franco.commands.system",
    "franco.commands.apps", "franco.commands.security",
    "franco.commands.files", "franco.commands.web",
    "franco.security.scanner", "franco.security.passwords",
    "franco.security.crypto", "franco.security.offensive",
    "franco.ui.renderer", "franco.ui.themes", "franco.ui.particles",
    "franco.ui.vision",
    "franco.integrations.earthquakes", "franco.integrations.notifications",
    "franco.integrations.mobile", "franco.integrations.remote",
    "franco.integrations.home_assistant", "franco.integrations.proactive",
    "franco.integrations.email",
    "franco.integrations.jarvis_bridge",
    "franco.integrations.jarvis_services",
]


@pytest.mark.parametrize("mod", MODULES)
def test_module_imports(mod):
    m = importlib.import_module(mod)
    assert hasattr(m, "__all__") or mod == "franco"


def test_expected_symbols():
    from franco.security.scanner import NetworkScanner
    from franco.ai.claude import ClaudeAIClient
    from franco.core.exceptions import FrancoException
    from franco.integrations.jarvis_bridge import JarvisBridge
    from franco.integrations.jarvis_services import JarvisServices
    from franco.capabilities import capability_catalog
    assert NetworkScanner and ClaudeAIClient and JarvisBridge and JarvisServices and capability_catalog and issubclass(FrancoException, Exception)
