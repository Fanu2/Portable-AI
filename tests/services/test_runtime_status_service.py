from portable_ai.runtimes.runtime_provider_registry import (
    RuntimeProviderRegistry,
)
from portable_ai.services.runtime_status_service import (
    RuntimeStatusService,
)


class HealthyRuntime:

    def health(self):
        return True


class OfflineRuntime:

    def health(self):
        return False


def test_runtime_status_service_reports_status():
    registry = RuntimeProviderRegistry()

    registry.register(
        "online",
        HealthyRuntime(),
    )

    registry.register(
        "offline",
        OfflineRuntime(),
    )

    service = RuntimeStatusService(
        registry
    )

    assert service.status() == {
        "online": True,
        "offline": False,
    }
