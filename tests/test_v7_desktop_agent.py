import json
import time

from franco.v7.desktop_agent import DesktopAgent
from franco.v7.intent import IntentParser


def eventually(predicate, timeout=2):
    deadline = time.monotonic() + timeout
    while not predicate():
        assert time.monotonic() < deadline
        time.sleep(.005)


class FakeImage:
    def save(self, target, format):
        assert format == "PNG"
        target.write(b"png")


class Automation:
    def __init__(self):
        self.actions = []

    def screenshot(self):
        return FakeImage()

    def click(self, **kwargs):
        self.actions.append(("click", kwargs))

    def doubleClick(self, **kwargs):
        self.actions.append(("double", kwargs))

    def hotkey(self, *keys):
        self.actions.append(("hotkey", keys))

    def press(self, key):
        self.actions.append(("press", key))

    def write(self, text, interval):
        self.actions.append(("write", text, interval))


class Brain:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def decide_screen(self, prompt, image, *, system):
        self.calls.append((prompt, image, system))
        return json.dumps(self.responses.pop(0))


def test_desktop_loop_observes_after_action_and_finishes():
    automation = Automation()
    brain = Brain([
        {"action": "click", "x": 40, "y": 80, "reason": "apri"},
        {"action": "done", "reason": "Obiettivo verificato"},
    ])
    agent = DesktopAgent(brain, automation=automation, step_pause=0)

    assert "ha preso" in agent.start("apri il menu")
    eventually(lambda: agent.status() == "Obiettivo verificato")

    assert automation.actions == [("click", {"x": 40, "y": 80})]
    assert len(brain.calls) == 2


def test_sensitive_step_waits_for_explicit_confirmation():
    automation = Automation()
    brain = Brain([
        {"action": "confirm", "reason": "invio esterno",
         "next_action": {"action": "type", "text": "ciao"}},
        {"action": "done", "reason": "Completato"},
    ])
    agent = DesktopAgent(brain, automation=automation, step_pause=0)

    agent.start("prepara il testo")
    eventually(lambda: agent.status().startswith("Serve conferma"))
    assert automation.actions == []
    assert "Conferma ricevuta" in agent.confirm()
    eventually(lambda: agent.status() == "Completato")
    assert automation.actions[0][:2] == ("write", "ciao")


def test_desktop_intent_marks_external_goals_for_confirmation():
    parser = IntentParser()
    safe = parser.parse("usa computer use per aprire il menu impostazioni")
    sensitive = parser.parse("usa computer use per pubblica il post")

    assert safe.name == sensitive.name == "desktop_goal"
    assert not safe.requires_confirmation
    assert sensitive.requires_confirmation
    assert parser.parse("ferma computer use").name == "desktop_stop"
    assert parser.parse("stato computer use").name == "desktop_status"
