from portable_ai.services.runtime_monitor_service import (
    RuntimeMonitorService,
)


class FakeHealthService:

    def snapshot(
        self,
        runtime_name,
    ):
        class Snapshot:
            pass

        snapshot = Snapshot()
        snapshot.runtime_name = runtime_name

        return snapshot


def test_runtime_monitor_returns_snapshot():

    monitor = RuntimeMonitorService(
        FakeHealthService()
    )

    snapshot = monitor.check(
        "ollama"
    )

    assert (
        snapshot.runtime_name
        == "ollama"
    )
