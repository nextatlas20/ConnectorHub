from vector_echo.config import endpoint


def test_endpoint_is_read(monkeypatch):
    monkeypatch.setenv("VECTOR_ECHO_ENDPOINT", "local")
    assert endpoint() == "local"
