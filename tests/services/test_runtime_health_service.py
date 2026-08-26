from portable_ai.models.runtime_health import (
    RuntimeHealth,
)

from portable_ai.runtimes.runtime_provider_registry import (
    RuntimeProviderRegistry,
)

from portable_ai.services.runtime_health_service import (
    RuntimeHealthService,
)


class OnlineRuntime:

    def health(self):
        return True


class OfflineRuntime:

    def health(self):
        return False


def test_runtime_health_service_reports_online():

    registry = RuntimeProviderRegistry()

    registry.register(
        "online",
        OnlineRuntime(),
    )

    service = RuntimeHealthService(
        registry
    )

    assert (
        service.status("online")
        == RuntimeHealth.ONLINE
    )


def test_runtime_health_service_reports_offline():

    registry = RuntimeProviderRegistry()

    registry.register(
        "offline",
        OfflineRuntime(),
    )

    service = RuntimeHealthService(
        registry
    )

    assert (
        service.status("offline")
        == RuntimeHealth.OFFLINE
    )


def test_runtime_health_service_reports_unknown():

    registry = RuntimeProviderRegistry()

    service = RuntimeHealthService(
        registry
    )

    assert (
        service.status("missing")
        == RuntimeHealth.UNKNOWN
    )
