from portable_ai.models.runtime_health import (
    RuntimeHealth,
)

from portable_ai.services.runtime_monitor_service import (
    RuntimeMonitorService,
)


class FakeHealthService:

    def snapshot(
        self,
        runtime_name,
    ):
        class Snapshot:
            health = RuntimeHealth.ONLINE

        return Snapshot()


def test_runtime_monitor_service_checks_runtime():

    monitor = RuntimeMonitorService(
        FakeHealthService()
    )

    result = monitor.check(
        "ollama"
    )

    assert (
        result.health
        == RuntimeHealth.ONLINE
    )
