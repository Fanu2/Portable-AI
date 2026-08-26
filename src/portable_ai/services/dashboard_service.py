from portable_ai.models.runtime_health_snapshot import (
    RuntimeHealthSnapshot,
)

from portable_ai.services.runtime_service import (
    RuntimeService,
)

from portable_ai.services.runtime_status_service import (
    RuntimeStatusService,
)

from portable_ai.services.runtime_health_service import (
    RuntimeHealthService,
)


class DashboardService:
    """
    Provides application summary data.
    """

    def __init__(
        self,
        runtime_service: RuntimeService,
        runtime_status_service: RuntimeStatusService,
        runtime_health_service: RuntimeHealthService,
    ) -> None:
        self._runtime_service = runtime_service
        self._runtime_status_service = runtime_status_service
        self._runtime_health_service = runtime_health_service

    def summary(self) -> dict:
        return {
            "runtimes": self._runtime_status_service.status(),
            "available_runtime_count": len(
                self._runtime_service.available_runtimes()
            ),
        }

    def runtime_health_snapshot(
        self,
        runtime_name: str,
    ) -> RuntimeHealthSnapshot:
        return self._runtime_health_service.snapshot(
            runtime_name
        )
