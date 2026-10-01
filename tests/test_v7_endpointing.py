from franco.v7.endpointing import AdaptiveEndpointDetector


def test_complete_sentence_finishes_after_short_pause():
    detector = AdaptiveEndpointDetector()
    assert detector.decide("Apri la mappa del mondo", .9).should_finalize is True


def test_truncated_sentence_waits_five_seconds():
    detector = AdaptiveEndpointDetector()
    early = detector.decide("Apri la mappa e", 2.5)
    late = detector.decide("Apri la mappa e", 5.0)
    assert early.should_finalize is False
    assert early.reason == "frase_troncata"
    assert late.should_finalize is True


def test_filler_keeps_microphone_open():
    detector = AdaptiveEndpointDetector()
    decision = detector.decide("allora ehm", 1.5)
    assert decision.should_finalize is False
    assert decision.wait_seconds == 3.5
