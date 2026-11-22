from orion_relay.delivery import backoff_seconds, max_inflight


def test_backoff_grows():
    assert backoff_seconds(3) > backoff_seconds(1)


def test_default_inflight():
    assert max_inflight() == 64
