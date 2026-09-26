from franco.live_canvas import normalize_canvas_command


def test_canvas_understands_synonyms_and_asr_variants():
    assert "cerchio" in normalize_canvas_command("creami una sfera gialla")
    assert "cerchio" in normalize_canvas_command("creami una sphera gialla")
    assert "razzo" in normalize_canvas_command("disegna un rasso")
    assert "stella" in normalize_canvas_command("aggiungi una stellina")


def test_canvas_preserves_numbers_for_dimensions():
    assert normalize_canvas_command("crea un quadrato blu 200 120").endswith("200 120")
