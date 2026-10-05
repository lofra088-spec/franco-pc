import json

from franco.v7.intent import IntentParser
from franco.v7.self_improve import SelfImprover


class BrainStub:
    def __init__(self, payload):
        self.payloads = payload if isinstance(payload, list) else [payload]
        self.prompts = []

    def complete(self, prompt, *, system, max_tokens=2000, temperature=.2):
        self.prompts.append(prompt)
        index = min(len(self.prompts) - 1, len(self.payloads) - 1)
        return self.payloads[index]


def make_root(tmp_path):
    root = tmp_path / "franco"
    (root / "v7").mkdir(parents=True)
    (root / "v7" / "mod.py").write_text("def add(a, b):\n    return a - b\n", encoding="utf-8")
    return root


def test_intent_recognizes_self_improve_and_revert():
    parser = IntentParser()
    assert parser.parse("risolvi questo bug nel tuo codice").name == "self_improve"
    assert parser.parse("migliora te stesso").name == "self_improve"
    assert parser.parse("annulla l'ultimo miglioramento").name == "revert_improve"
    assert parser.parse("conferma miglioramento").name == "apply_improvement"
    assert parser.parse("annulla miglioramento").name == "cancel_improvement"
    assert parser.parse("apri chrome").name == "open_app"


def test_prepare_never_writes_then_confirm_applies_and_verifies(tmp_path):
    root = make_root(tmp_path)
    payload = json.dumps({
        "summary": "Correggo la sottrazione in somma",
        "changes": [{"path": "v7/mod.py", "action": "patch",
                     "old": "    return a - b", "new": "    return a + b"}],
    })
    improver = SelfImprover(BrainStub(payload), root=root, log_dir=tmp_path / "logs",
                            verifier=lambda: (True, "ok"))
    message = improver.prepare("risolvi questo bug nel tuo codice")

    assert "return a - b" in (root / "v7" / "mod.py").read_text(encoding="utf-8")
    assert "conferma miglioramento" in message
    message = improver.apply_pending()
    assert "return a + b" in (root / "v7" / "mod.py").read_text(encoding="utf-8")
    assert "v7/mod.py" in message
    assert list((tmp_path / "logs").glob("run-*.json"))


def test_solve_rolls_back_when_verification_fails(tmp_path):
    root = make_root(tmp_path)
    payload = json.dumps({
        "summary": "Provo una modifica rotta",
        "changes": [{"path": "v7/mod.py", "action": "patch",
                     "old": "    return a - b", "new": "    return a + b"}],
    })
    improver = SelfImprover(BrainStub(payload), root=root, log_dir=tmp_path / "logs",
                            verifier=lambda: (False, "import rotto"))
    improver.prepare("migliora te stesso")
    message = improver.apply_pending()

    assert (root / "v7" / "mod.py").read_text(encoding="utf-8") == \
        "def add(a, b):\n    return a - b\n"
    assert "ripristinata" in message
    assert not list((tmp_path / "logs").glob("run-*.json"))


def test_revert_last_restores_previous_content(tmp_path):
    root = make_root(tmp_path)
    payload = json.dumps({
        "summary": "Somma",
        "changes": [{"path": "v7/mod.py", "action": "patch",
                     "old": "    return a - b", "new": "    return a + b"}],
    })
    improver = SelfImprover(BrainStub(payload), root=root, log_dir=tmp_path / "logs",
                            verifier=lambda: (True, "ok"))
    improver.prepare("risolvi questo bug nel tuo codice")
    improver.apply_pending()
    result = improver.revert_last()

    assert "return a - b" in (root / "v7" / "mod.py").read_text(encoding="utf-8")
    assert "ripristinati" in result


def test_path_outside_package_is_rejected(tmp_path):
    root = make_root(tmp_path)
    payload = json.dumps({
        "summary": "Evasione",
        "changes": [{"path": "../evil.py", "action": "write", "content": "print(1)"}],
    })
    improver = SelfImprover(BrainStub(payload), root=root, log_dir=tmp_path / "logs",
                            verifier=lambda: (True, "ok"))
    message = improver.prepare("sistemati")

    assert "non consentito" in message
    assert not (tmp_path / "evil.py").exists()


def test_bad_patch_is_rejected_without_touching_files(tmp_path):
    root = make_root(tmp_path)
    payload = json.dumps({
        "summary": "Patch sbagliata",
        "changes": [{"path": "v7/mod.py", "action": "patch",
                     "old": "testo che non esiste", "new": "print(1)"}],
    })
    improver = SelfImprover(BrainStub(payload), root=root, log_dir=tmp_path / "logs",
                            verifier=lambda: (True, "ok"))
    improver.prepare("correggi questo bug nel tuo codice")
    message = improver.apply_pending()

    assert "non applicabile" in message
    assert (root / "v7" / "mod.py").read_text(encoding="utf-8") == \
        "def add(a, b):\n    return a - b\n"


def test_repair_retry_recovers_from_invalid_json(tmp_path):
    root = make_root(tmp_path)
    good = json.dumps({
        "summary": "Somma corretta",
        "changes": [{"path": "v7/mod.py", "action": "patch",
                     "old": "    return a - b", "new": "    return a + b"}],
    })
    improver = SelfImprover(BrainStub(["ecco come potrei farlo...", good]),
                            root=root, log_dir=tmp_path / "logs",
                            verifier=lambda: (True, "ok"))
    improver.prepare("risolvi questo bug nel tuo codice")
    message = improver.apply_pending()

    assert "return a + b" in (root / "v7" / "mod.py").read_text(encoding="utf-8")
    assert "v7/mod.py" in message


def test_list_shaped_changes_are_accepted(tmp_path):
    root = make_root(tmp_path)
    payload = json.dumps([
        {"path": "v7/mod.py", "action": "patch",
         "old": "    return a - b", "new": "    return a + b"},
    ])
    improver = SelfImprover(BrainStub(payload), root=root, log_dir=tmp_path / "logs",
                            verifier=lambda: (True, "ok"))
    improver.prepare("sistemati il codice")
    message = improver.apply_pending()

    assert "return a + b" in (root / "v7" / "mod.py").read_text(encoding="utf-8")
    assert "v7/mod.py" in message


def test_cancel_pending_keeps_files_untouched(tmp_path):
    root = make_root(tmp_path)
    payload = json.dumps({
        "summary": "Somma",
        "changes": [{"path": "v7/mod.py", "action": "patch",
                     "old": "    return a - b", "new": "    return a + b"}],
    })
    improver = SelfImprover(BrainStub(payload), root=root, log_dir=tmp_path / "logs",
                            verifier=lambda: (True, "ok"))
    improver.prepare("migliora il tuo codice")
    assert "nessun file" in improver.cancel_pending()
    assert "return a - b" in (root / "v7" / "mod.py").read_text(encoding="utf-8")
    assert "nessun miglioramento" in improver.apply_pending()
