from franco.v7.actions import ActionRegistry
from franco.v7.runtime import FrancoRuntime
import subprocess
import sys
import os
from pathlib import Path


class BrainStub:
    def __init__(self):
        self.calls = []

    def answer(self, text, *, context):
        self.calls.append((text, context))
        return "Risposta utile"


def test_partial_transcript_prepares_but_never_executes():
    calls = []
    actions = ActionRegistry()
    actions.register("open_app", lambda name: calls.append(name) or f"Apro {name}")
    runtime = FrancoRuntime(BrainStub(), actions)

    prepared = runtime.observe_partial("apri OBS")

    assert prepared.intent.name == "open_app"
    assert calls == []


def test_final_local_action_is_immediate_and_skips_brain():
    brain = BrainStub()
    actions = ActionRegistry()
    actions.register("web_search", lambda query: f"Cerco {query}")
    runtime = FrancoRuntime(brain, actions)

    reply = runtime.submit_final("cerca su Google mod horror Minecraft")

    assert reply.text == "Cerco mod horror Minecraft"
    assert reply.executed is True
    assert brain.calls == []


def test_open_conversation_uses_brain_and_history():
    brain = BrainStub()
    runtime = FrancoRuntime(brain)

    reply = runtime.submit_final("spiegami perché il cielo è blu")

    assert reply.text == "Risposta utile"
    assert runtime.history[-1]["role"] == "assistant"


def test_clean_v7_package_does_not_load_legacy_monolith():
    code = "import franco.v7, sys; assert 'franco._monolith' not in sys.modules"
    root = Path(__file__).resolve().parents[1]
    env = dict(os.environ, PYTHONPATH=str(root / "src"))
    subprocess.run([sys.executable, "-c", code], check=True, env=env)


def test_history_is_bounded_and_brain_errors_do_not_crash_runtime():
    brain = BrainStub()
    runtime = FrancoRuntime(brain)
    for index in range(20):
        runtime.submit_final(f"domanda numero {index}")
    assert len(runtime.history) == 16

    class BrokenBrain:
        def answer(self, text, *, context):
            raise RuntimeError("offline")

    reply = FrancoRuntime(BrokenBrain()).submit_final("dimmi qualcosa")
    assert "comandi locali" in reply.text
