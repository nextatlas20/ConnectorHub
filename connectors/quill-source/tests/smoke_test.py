from quill_source.config import endpoint


def test_endpoint_is_read(monkeypatch):
    monkeypatch.setenv("QUILL_SOURCE_ENDPOINT", "local")
    assert endpoint() == "local"
