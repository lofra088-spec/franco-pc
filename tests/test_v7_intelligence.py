import io
import json
from pathlib import Path

import pytest

from franco.v7.intelligence import IntelligenceError, PublicIntelligence
from franco.v7.intent import IntentParser


class JsonResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        self.close()


def fake_open(payload):
    def open_response(_request, timeout=0):
        assert timeout > 0
        return JsonResponse(json.dumps(payload).encode())
    return open_response


def test_intents_for_map_people_and_image_are_deterministic():
    parser = IntentParser()
    cameras = parser.parse("mostrami le telecamere di Catanzaro")
    flights = parser.parse("fammi vedere tutti i voli sopra Boston")
    person = parser.parse("cerca una persona Mario Rossi")
    image = parser.parse(r"geolocalizza questa foto C:\foto\piazza.jpg")

    assert (cameras.name, cameras.arguments) == (
        "map_search", {"location": "Catanzaro", "layer": "telecamere"})
    assert (flights.name, flights.arguments) == (
        "map_search", {"location": "Boston", "layer": "voli"})
    assert person.name == "person_research"
    assert person.arguments["name"] == "Mario Rossi"
    assert image.name == "image_geolocation"


def test_map_geocodes_location_and_opens_argos_deep_link():
    opened = []
    payload = {"features": [{"geometry": {"coordinates": [16.59, 38.91]}}]}
    intel = PublicIntelligence(open_url=opened.append, urlopen=fake_open(payload))

    result = intel.open_map("Catanzaro", "telecamere")

    assert opened == ["https://www.argosatlas.com/map/#view=38.910000,16.590000,11"]
    assert "telecamere pubbliche" in result


def test_person_report_is_sourced_and_excludes_sensitive_query_types():
    opened = []
    payload = {"query": {"pages": {"1": {
        "title": "Mario Rossi", "extract": "Profilo pubblico verificabile.",
        "fullurl": "https://it.wikipedia.org/wiki/Mario_Rossi",
    }}}}
    intel = PublicIntelligence(open_url=opened.append, urlopen=fake_open(payload))

    result = intel.research_person("Mario Rossi")

    assert opened == ["https://maxintel.org/person.html"]
    assert "Possibile corrispondenza pubblica" in result
    assert "Fonte verificabile" in result
    assert "dati privati" in result
    with pytest.raises(IntelligenceError):
        intel.research_person("mario@example.com")
    with pytest.raises(IntelligenceError):
        intel.research_person("3331234567")


def test_geospy_without_key_opens_official_site(monkeypatch, tmp_path: Path):
    monkeypatch.delenv("GEOSPY_API_KEY", raising=False)
    image = tmp_path / "foto.jpg"
    image.write_bytes(b"not decoded locally")
    opened = []
    intel = PublicIntelligence(open_url=opened.append)

    result = intel.geolocate_image(str(image))

    assert opened == ["https://geospy.ai/"]
    assert "GEOSPY_API_KEY" in result

