from portable_ai.contracts.runtime_monitor import (
    RuntimeMonitor,
)


def test_runtime_monitor_is_abstract():

    assert RuntimeMonitor.__abstractmethods__
