from portable_ai.contracts.runtime_monitor import (
    RuntimeMonitor,
)

from portable_ai.models.runtime_health_snapshot import (
    RuntimeHealthSnapshot,
)

from portable_ai.services.runtime_health_service import (
    RuntimeHealthService,
)


class RuntimeMonitorService(RuntimeMonitor):
    """
    Provides runtime monitoring boundary.
    """

    def __init__(
        self,
        health_service: RuntimeHealthService,
    ) -> None:
        self._health_service = health_service

    def check(
        self,
        runtime_name: str,
    ) -> RuntimeHealthSnapshot:
        return self._health_service.snapshot(
            runtime_name
        )
