from nova_bridge.config import endpoint


def test_endpoint_is_read(monkeypatch):
    monkeypatch.setenv("NOVA_BRIDGE_ENDPOINT", "local")
    assert endpoint() == "local"
