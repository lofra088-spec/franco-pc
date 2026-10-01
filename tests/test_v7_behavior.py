"""Focused checks for the Franco V7 interaction contract."""
from types import SimpleNamespace
from unittest.mock import Mock

from franco._monolith import CommandEngine, FrancoCore


class StateStub:
    def __init__(self):
        self.values = {}

    def set(self, key, value, notify=True):
        self.values[key] = value

    def get(self, key, default=None):
        return self.values.get(key, default)


def test_partial_voice_prepares_app_without_launching_it():
    state = StateStub()
    launcher = Mock()
    launcher.find.return_value = ("obs studio", r"C:\OBS\obs64.exe")
    core = SimpleNamespace(
        state=state,
        latency_router=SimpleNamespace(classify=lambda _text: "fast"),
        app_launcher=launcher,
    )

    FrancoCore._on_voice_partial(
        core, SimpleNamespace(data={"text": "apri OBS"})
    )

    assert state.values["partial_plan"]["intent"] == "open_app"
    assert state.values["partial_plan"]["resolved_app"][0] == "obs studio"
    launcher.find.assert_called_once_with("OBS")


def test_self_improvement_requires_explicit_confirmation():
    state = StateStub()
    engine = SimpleNamespace(state=state)

    response = CommandEngine._cmd_targeted_self_improve(
        engine, "impara a esportare un documento"
    )

    assert "conferma miglioramento" in response.lower()
    assert state.values["pending_self_improve"]["request"] == "impara a esportare un documento"


def test_desktop_executor_rejects_unknown_actions():
    engine = SimpleNamespace(vision=Mock())

    result = CommandEngine._execute_desktop_action(
        engine, {"action": "powershell", "testo": "comando"}
    )

    assert "non consentita" in result
    engine.vision.assert_not_called()
