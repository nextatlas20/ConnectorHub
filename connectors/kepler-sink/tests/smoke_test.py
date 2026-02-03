from kepler_sink.config import endpoint


def test_endpoint_is_read(monkeypatch):
    monkeypatch.setenv("KEPLER_SINK_ENDPOINT", "local")
    assert endpoint() == "local"
