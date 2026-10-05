"""Desktop concurrency tests using only deterministic, in-memory adapters."""
from threading import Event, Thread, current_thread
from time import monotonic
from types import SimpleNamespace

import pytest

from franco.v7.desktop_controller import DesktopController


def eventually(predicate, timeout=2):
    deadline = monotonic() + timeout
    while not predicate():
        assert monotonic() < deadline, "worker did not reach the expected state"
        Event().wait(.005)


def responsive(call):
    """A blocked UI operation fails promptly instead of hanging this suite."""
    done = Event()
    result = []

    def run():
        result.append(call())
        done.set()

    Thread(target=run, daemon=True).start()
    assert done.wait(.5), "UI-facing operation blocked on an adapter/runtime"
    return result[0]


class RuntimeStub:
    def __init__(self, *, blocked=False, fail=False):
        self.calls = []
        self.partials = []
        self.threads = []
        self.started = Event()
        self.release = Event()
        if not blocked:
            self.release.set()
        self.fail = fail

    def submit_final(self, text):
        self.calls.append(text)
        self.threads.append(current_thread().name)
        self.started.set()
        self.release.wait(5)
        if self.fail:
            raise RuntimeError("azione non disponibile")
        return SimpleNamespace(text="Risposta: " + text)

    def observe_partial(self, text):
        self.partials.append(text)
        self.threads.append(current_thread().name)


class SpeechStub:
    def __init__(self, *, blocked=False, fail=False):
        self.said = []
        self.started = Event()
        self.release = Event()
        if not blocked:
            self.release.set()
        self.stopped = Event()
        self.closed = Event()
        self.close_calls = 0
        self.fail = fail

    def say(self, text):
        self.said.append(text)
        self.started.set()
        self.release.wait(5)
        if self.fail:
            raise RuntimeError("altoparlante assente")

    def stop(self):
        self.stopped.set()

    def close(self):
        self.close_calls += 1
        self.closed.set()


class MicrophoneStub:
    def __init__(self, *, blocked=False, fail=False):
        self.sessions = []
        self.started = Event()
        self.release = Event()
        if not blocked:
            self.release.set()
        self.stopped = Event()
        self.closed = Event()
        self.close_calls = 0
        self.fail = fail

    def start(self, on_partial, on_final, on_status):
        self.sessions.append(SimpleNamespace(partial=on_partial, final=on_final, status=on_status))
        self.started.set()
        self.release.wait(5)
        if self.fail:
            raise RuntimeError("nessun dispositivo di ingresso")

    def stop(self):
        self.stopped.set()

    def close(self):
        self.close_calls += 1
        self.closed.set()


@pytest.fixture
def controllers():
    created = []

    def make(runtime=None, **kwargs):
        controller = DesktopController(runtime or RuntimeStub(), **kwargs)
        created.append(controller)
        return controller

    yield make
    for controller in created:
        controller.close()
        controller.runtime.release.set()
        for device in controller._devices.values():
            release = getattr(device, "release", None)
            if release is not None:
                release.set()
    for controller in created:
        eventually(lambda controller=controller: all(
            not thread.is_alive() for thread in controller._threads.values()
        ))


def messages(events, role):
    return [event["text"] for event in events
            if event["type"] == "message" and event["role"] == role]


def test_initial_state_and_lazy_optional_devices(controllers):
    factories = []
    controller = controllers(speech=lambda: factories.append("speech"),
                             microphone=lambda: factories.append("microphone"))
    assert not controller.microphone_enabled
    assert controller.voice_enabled
    assert not controller.busy
    assert not controller.closed
    assert factories == []
    assert controller.drain_events() == [{"type": "state", "busy": False,
                                         "microphone_enabled": False, "voice_enabled": True,
                                         "status": "Pronto"}]
    assert not controller.submit("")
    assert not controller.submit("   ")
    assert not controller.submit(None)
    assert not controller.submit("x" * (controller.MAX_TEXT_CHARS + 1))
    assert controller.runtime.calls == []
    assert controller.drain_events()[0]["type"] == "error"


def test_blocked_runtime_never_blocks_ui_or_accepts_unbounded_work(controllers):
    runtime = RuntimeStub(blocked=True)
    speech = SpeechStub()
    controller = controllers(runtime, speech=speech)
    assert responsive(lambda: controller.submit("prima")) is True
    assert runtime.started.wait(1)
    assert controller.busy
    for _ in range(300):
        assert not controller.submit("non accodata")
    assert len(controller.drain_events()) <= controller.MAX_EVENTS
    assert responsive(controller.toggle_voice) is False
    assert responsive(controller.drain_events) is not None
    runtime.release.set()
    eventually(lambda: not controller.busy)
    assert runtime.calls == ["prima"]
    assert messages(controller.drain_events(), "assistant") == ["Risposta: prima"]
    assert speech.said == []
    assert runtime.threads == ["franco-v7-command"]


def test_cancel_suppresses_late_reply_and_audio_without_lying_about_busy(controllers):
    runtime = RuntimeStub(blocked=True)
    speech = SpeechStub()
    controller = controllers(runtime, speech=speech)
    assert controller.submit("vecchia")
    assert runtime.started.wait(1)
    responsive(controller.cancel)
    assert controller.busy  # Python cannot interrupt the running call.
    assert not controller.submit("non accodare dietro al modello bloccato")
    controller.drain_events()
    runtime.release.set()
    eventually(lambda: not controller.busy)
    assert messages(controller.drain_events(), "assistant") == []
    assert speech.said == []
    assert controller.submit("nuova")
    eventually(lambda: not controller.busy)
    assert messages(controller.drain_events(), "assistant") == ["Risposta: nuova"]


def test_cancel_removes_work_not_yet_taken_by_worker(controllers):
    controller = controllers()
    # Hold the controller condition to make the queued-before-dispatch state exact.
    with controller._cv:
        assert controller.submit("non eseguire")
        controller.cancel()
        assert not controller.busy
    assert controller.submit("esegui")
    eventually(lambda: not controller.busy)
    assert controller.runtime.calls == ["esegui"]


def test_failed_action_is_reported_and_next_turn_can_run(controllers):
    runtime = RuntimeStub(fail=True)
    controller = controllers(runtime)
    assert controller.submit("azione")
    eventually(lambda: not controller.busy)
    assert any("azione non disponibile" in event.get("text", "")
               for event in controller.drain_events() if event["type"] == "error")
    runtime.fail = False
    assert controller.submit("successiva")
    eventually(lambda: not controller.busy)
    assert messages(controller.drain_events(), "assistant") == ["Risposta: successiva"]


def test_voice_mute_stops_blocked_speech_and_text_keeps_working(controllers):
    speech = SpeechStub(blocked=True)
    controller = controllers(speech=speech)
    controller.submit("prima")
    assert speech.started.wait(1)
    eventually(lambda: not controller.busy)
    speech.stopped.clear()
    assert responsive(controller.toggle_voice) is False
    assert speech.stopped.wait(1)
    assert not controller.microphone_enabled
    assert controller.submit("seconda")
    eventually(lambda: not controller.busy)
    assert messages(controller.drain_events(), "assistant") == ["Risposta: prima", "Risposta: seconda"]
    assert speech.said == ["Risposta: prima"]
    speech.release.set()


def test_muted_response_is_not_replayed_when_voice_is_enabled(controllers):
    speech = SpeechStub()
    controller = controllers(speech=speech)
    assert controller.toggle_voice() is False
    controller.submit("silenziosa")
    eventually(lambda: not controller.busy)
    assert controller.toggle_voice() is True
    controller.submit("parlata")
    assert speech.started.wait(1)
    assert speech.said == ["Risposta: parlata"]


def test_failed_voice_does_not_lose_text_or_block_subsequent_turns(controllers):
    speech = SpeechStub(fail=True)
    controller = controllers(speech=speech)
    controller.submit("domanda")
    assert speech.started.wait(1)
    eventually(lambda: not controller.busy)
    eventually(lambda: any(event["type"] == "error" for event in controller._events))
    events = controller.drain_events()
    assert messages(events, "assistant") == ["Risposta: domanda"]
    assert any("altoparlante assente" in event.get("text", "") for event in events)
    assert controller.submit("ancora")


def test_microphone_start_is_async_and_muting_flushes_stale_callbacks(controllers):
    microphone = MicrophoneStub(blocked=True)
    controller = controllers(microphone=microphone)
    assert responsive(controller.toggle_microphone) is True
    assert microphone.started.wait(1)
    old = microphone.sessions[0]
    old.partial("apri")
    assert responsive(controller.toggle_microphone) is False
    assert microphone.stopped.wait(1)
    old.partial("apri qualcosa")
    old.final("apri qualcosa")
    old.status({"status": "vecchio ascolto"})
    events = controller.drain_events()
    assert [event["text"] for event in events if event["type"] == "partial"] == [""]
    assert not messages(events, "user")
    assert controller.runtime.calls == []
    assert controller.voice_enabled
    microphone.release.set()


def test_old_microphone_generation_cannot_submit_after_reenable(controllers):
    microphone = MicrophoneStub()
    controller = controllers(microphone=microphone)
    controller.toggle_microphone()
    assert microphone.started.wait(1)
    old = microphone.sessions[0]
    assert controller.toggle_microphone() is False
    assert controller.toggle_microphone() is True
    eventually(lambda: len(microphone.sessions) == 2)
    old.final("vecchia")
    microphone.sessions[1].final("nuova")
    eventually(lambda: not controller.busy)
    assert controller.runtime.calls == ["nuova"]


def test_partials_prepare_on_same_worker_and_never_execute(controllers):
    microphone = MicrophoneStub()
    controller = controllers(microphone=microphone)
    controller.toggle_microphone()
    assert microphone.started.wait(1)
    session = microphone.sessions[0]
    session.partial("apri OBS")
    eventually(lambda: bool(controller.runtime.partials))
    assert controller.runtime.partials == ["apri OBS"]
    assert controller.runtime.calls == []
    session.status({"status": "Sto ascoltando"})
    assert any(event.get("status") == "Sto ascoltando" for event in controller.drain_events())
    session.final("apri OBS")
    eventually(lambda: not controller.busy)
    assert controller.runtime.calls == ["apri OBS"]
    assert set(controller.runtime.threads) == {"franco-v7-command"}


def test_partial_flood_is_coalesced_and_bounded_behind_blocked_runtime(controllers):
    runtime = RuntimeStub(blocked=True)
    microphone = MicrophoneStub()
    controller = controllers(runtime, microphone=microphone)
    controller.toggle_microphone()
    assert microphone.started.wait(1)
    controller.submit("bloccata")
    assert runtime.started.wait(1)
    session = microphone.sessions[0]
    for index in range(300):
        session.partial(str(index) + "x" * 20_000)
        session.status({"status": "s" * 1000})
    assert len(controller._events) <= controller.MAX_EVENTS
    assert len(controller._partial[1]) <= controller.MAX_PARTIAL_CHARS
    events = controller.drain_events()
    assert len([event for event in events if event["type"] == "partial"]) == 1
    assert len([event for event in events if event["type"] == "state"]) == 1
    assert max(len(event.get("status", "")) for event in events) <= controller.MAX_STATUS_CHARS
    controller.toggle_microphone()
    runtime.release.set()
    eventually(lambda: not controller.busy)
    assert runtime.partials == []


def test_microphone_failure_returns_to_off_and_reports_error(controllers):
    microphone = MicrophoneStub(fail=True)
    controller = controllers(microphone=microphone)
    controller.toggle_microphone()
    assert microphone.started.wait(1)
    eventually(lambda: not controller.microphone_enabled)
    events = controller.drain_events()
    assert any("nessun dispositivo" in event.get("text", "") for event in events)
    assert controller.submit("testo ancora disponibile")


def test_microphone_status_error_turns_it_off_and_preserves_chat(controllers):
    microphone = MicrophoneStub()
    controller = controllers(microphone=microphone)
    assert controller.toggle_microphone()
    assert microphone.started.wait(1)
    microphone.sessions[0].status({"status": "error", "text": "permesso negato"})
    eventually(lambda: not controller.microphone_enabled)
    events = controller.drain_events()
    assert any("permesso negato" in event.get("text", "") for event in events)
    assert controller.submit("scrivo dalla chat")


def test_missing_microphone_returns_false_and_is_honest(controllers):
    controller = controllers()
    assert not controller.toggle_microphone()
    assert not controller.microphone_enabled
    assert any(event["type"] == "error" for event in controller.drain_events())


@pytest.mark.parametrize("operation", ["cancel", "close"])
def test_lazy_speech_created_after_invalidation_never_speaks(controllers, operation):
    creating = Event()
    release_factory = Event()
    speech = SpeechStub()

    def factory():
        creating.set()
        release_factory.wait(5)
        return speech

    controller = controllers(speech=factory)
    controller.submit("obsoleta")
    assert creating.wait(1)
    responsive(getattr(controller, operation))
    release_factory.set()
    if operation == "close":
        assert speech.closed.wait(1)
    else:
        eventually(lambda: "speech" in controller._devices)
    assert speech.said == []


def test_close_during_lazy_microphone_creation_cleans_late_adapter(controllers):
    creating = Event()
    release_factory = Event()
    microphone = MicrophoneStub()

    def factory():
        creating.set()
        release_factory.wait(5)
        return microphone

    controller = controllers(microphone=factory)
    assert controller.toggle_microphone()
    assert creating.wait(1)
    responsive(controller.close)
    release_factory.set()
    assert microphone.closed.wait(1)
    assert microphone.sessions == []


def test_cancel_invalidates_ongoing_microphone_utterance(controllers):
    microphone = MicrophoneStub()
    controller = controllers(microphone=microphone)
    controller.toggle_microphone()
    assert microphone.started.wait(1)
    old = microphone.sessions[0]
    old.partial("richiesta incompleta")
    controller.cancel()
    old.final("richiesta da ignorare")
    eventually(lambda: len(microphone.sessions) == 2)
    assert controller.runtime.calls == []
    assert controller.microphone_enabled


def test_close_is_idempotent_nonblocking_and_discards_late_output(controllers):
    runtime = RuntimeStub(blocked=True)
    microphone = MicrophoneStub()
    speech = SpeechStub()
    controller = controllers(runtime, speech=speech, microphone=microphone)
    controller.toggle_microphone()
    assert microphone.started.wait(1)
    controller.submit("in corso")
    assert runtime.started.wait(1)
    responsive(controller.close)
    controller.close()
    assert controller.closed
    assert not controller.busy
    assert not controller.voice_enabled
    assert not controller.microphone_enabled
    assert not controller.submit("dopo chiusura")
    assert not controller.toggle_microphone()
    assert not controller.toggle_voice()
    assert microphone.closed.wait(1)
    assert speech.closed.wait(1)
    controller.drain_events()
    microphone.sessions[0].partial("tardiva")
    microphone.sessions[0].final("tardiva")
    runtime.release.set()
    eventually(lambda: "command" in controller._finished)
    assert controller.drain_events() == []
    assert speech.said == []
    assert speech.close_calls == microphone.close_calls == 1


def test_blocked_stop_does_not_block_ui_or_the_other_device(controllers):
    entered = Event()
    release_stop = Event()

    class BlockingSpeech(SpeechStub):
        def stop(self):
            entered.set()
            release_stop.wait(5)

    speech = BlockingSpeech()
    microphone = MicrophoneStub()
    controller = controllers(speech=speech, microphone=microphone)
    responsive(controller.toggle_voice)
    assert entered.wait(1)
    assert responsive(controller.toggle_microphone) is True
    assert microphone.started.wait(1)
    responsive(controller.close)
    assert microphone.closed.wait(1)
    release_stop.set()
    assert speech.closed.wait(1)


def test_adapter_cleanup_exceptions_cannot_crash_ui(controllers):
    class BrokenCleanup(SpeechStub):
        def stop(self):
            raise RuntimeError("stop guasto")

        def close(self):
            raise RuntimeError("chiusura guasta")

    controller = controllers(speech=BrokenCleanup())
    responsive(controller.toggle_voice)
    eventually(lambda: any(event["type"] == "error" for event in controller._events))
    responsive(controller.close)
    assert controller.closed


def test_class_adapters_are_instantiated_before_use(controllers):
    speeches, microphones = [], []

    class ClassSpeech(SpeechStub):
        def __init__(self):
            super().__init__()
            speeches.append(self)

    class ClassMicrophone(MicrophoneStub):
        def __init__(self):
            super().__init__()
            microphones.append(self)

    controller = controllers(speech=ClassSpeech, microphone=ClassMicrophone)
    assert controller.toggle_microphone() is True
    eventually(lambda: bool(microphones))
    assert microphones[0].started.wait(1)
    assert controller.toggle_microphone() is False
    assert microphones[0].stopped.wait(1)
    assert not [event for event in controller.drain_events()
                if event["type"] == "error" and "positional argument" in event.get("text", "")]
    controller.submit("ciao")
    eventually(lambda: not controller.busy)
    eventually(lambda: bool(speeches) and bool(speeches[0].said))
    assert speeches[0].said == ["Risposta: ciao"]
    responsive(controller.close)
    assert microphones[0].closed.wait(1)
    assert speeches[0].closed.wait(1)


def test_runtime_output_and_all_worker_counts_remain_bounded(controllers):
    runtime = RuntimeStub()
    runtime.submit_final = lambda text: SimpleNamespace(text="r" * 100_000)
    speech = SpeechStub()
    microphone = MicrophoneStub()
    controller = controllers(runtime, speech=speech, microphone=microphone)
    for _ in range(12):
        controller.toggle_microphone()
        controller.toggle_voice()
        assert controller.submit("domanda")
        eventually(lambda: not controller.busy)
    events = controller.drain_events()
    assert max(len(event.get("text", "")) for event in events) <= controller.MAX_TEXT_CHARS
    assert len(controller._threads) <= 5
    assert all(thread.daemon for thread in controller._threads.values())


def test_runtime_partial_failure_does_not_kill_command_worker(controllers):
    runtime = RuntimeStub()

    def bad_partial(text):
        raise RuntimeError("partial guasto")

    runtime.observe_partial = bad_partial
    microphone = MicrophoneStub()
    controller = controllers(runtime, microphone=microphone)
    controller.toggle_microphone()
    assert microphone.started.wait(1)
    microphone.sessions[0].partial("parziale")
    eventually(lambda: any(event["type"] == "error" for event in controller._events))
    microphone.sessions[0].final("completa")
    eventually(lambda: not controller.busy)
    assert runtime.calls == ["completa"]
