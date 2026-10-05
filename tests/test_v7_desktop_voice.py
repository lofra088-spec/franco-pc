from franco.v7.desktop_voice import DesktopSpeech, speech_text


def test_windows_speech_process_stays_alive_until_utterance_finishes():
    assert "Speak($text,0)" in DesktopSpeech._SCRIPT
    assert "Speak($text,16)" not in DesktopSpeech._SCRIPT


def test_speech_text_removes_urls_and_code_for_natural_voice():
    value = speech_text("Apri [la pagina](https://example.test) ```python\nprint(1)\n```")
    assert "https" not in value
    assert "print" not in value
    assert "la pagina" in value
