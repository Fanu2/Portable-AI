from portable_ai.models.runtime_health import (
    RuntimeHealth,
)

from portable_ai.services.runtime_readiness_service import (
    RuntimeReadinessService,
)


class FakeHealthService:

    def __init__(
        self,
        health,
    ) -> None:

        self._health = health

    def status(
        self,
        runtime_name,
    ):
        return self._health


def test_runtime_readiness_reports_ready_when_online():

    service = RuntimeReadinessService(
        FakeHealthService(
            RuntimeHealth.ONLINE
        )
    )

    result = service.check(
        "ollama"
    )

    assert result.runtime_name == "ollama"
    assert result.health == RuntimeHealth.ONLINE
    assert result.ready is True
    assert result.reason == "runtime online"


def test_runtime_readiness_reports_not_ready_when_offline():

    service = RuntimeReadinessService(
        FakeHealthService(
            RuntimeHealth.OFFLINE
        )
    )

    result = service.check(
        "ollama"
    )

    assert result.runtime_name == "ollama"
    assert result.health == RuntimeHealth.OFFLINE
    assert result.ready is False
    assert result.reason == "runtime not ready"


def test_runtime_readiness_reports_not_ready_when_unknown():

    service = RuntimeReadinessService(
        FakeHealthService(
            RuntimeHealth.UNKNOWN
        )
    )

    result = service.check(
        "missing"
    )

    assert result.ready is False


def test_runtime_readiness_reports_not_ready_when_degraded():

    service = RuntimeReadinessService(
        FakeHealthService(
            RuntimeHealth.DEGRADED
        )
    )

    result = service.check(
        "ollama"
    )

    assert result.ready is False
