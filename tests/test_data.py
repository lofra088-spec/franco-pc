"""The extracted data tables are valid JSON with content."""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "src" / "franco" / "data"


def test_data_files_present_and_parse():
    for name in ("ports.json", "http_codes.json", "apps.json", "themes.json"):
        payload = json.loads((DATA / name).read_text(encoding="utf-8"))
        assert isinstance(payload, dict)
