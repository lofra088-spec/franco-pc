import pytest

from franco.live_canvas import normalize_canvas_command, safe_calculate


def test_canvas_understands_synonyms_and_asr_variants():
    assert "cerchio" in normalize_canvas_command("creami una sfera gialla")
    assert "cerchio" in normalize_canvas_command("creami una sphera gialla")
    assert "razzo" in normalize_canvas_command("disegna un rasso")
    assert "stella" in normalize_canvas_command("aggiungi una stellina")


def test_canvas_preserves_numbers_for_dimensions():
    assert normalize_canvas_command("crea un quadrato blu 200 120").endswith("200 120")


@pytest.mark.parametrize(("expression", "expected"), [
    ("2 + 2", 4),
    ("(3 + 2) * 4", 20),
    ("10 / 4", 2.5),
    ("2**3", 8),
])
def test_safe_calculate_supports_arithmetic(expression, expected):
    assert safe_calculate(expression) == expected


def test_safe_calculate_rejects_python_code():
    with pytest.raises(ValueError):
        safe_calculate("__import__('os').system('whoami')")
