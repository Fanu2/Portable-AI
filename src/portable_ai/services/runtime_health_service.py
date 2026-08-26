from datetime import datetime

from portable_ai.models.runtime_health import (
    RuntimeHealth,
)

from portable_ai.models.runtime_health_snapshot import (
    RuntimeHealthSnapshot,
)


class RuntimeHealthService:
    """
    Converts runtime health checks into states.
    """

    def __init__(
        self,
        registry,
    ) -> None:
        self._registry = registry

    def status(
        self,
        runtime_name: str,
    ) -> RuntimeHealth:
        runtime = self._registry.get(
            runtime_name
        )

        if runtime is None:
            return RuntimeHealth.UNKNOWN

        if runtime.health():
            return RuntimeHealth.ONLINE

        return RuntimeHealth.OFFLINE

    def snapshot(
        self,
        runtime_name: str,
    ) -> RuntimeHealthSnapshot:
        return RuntimeHealthSnapshot(
            runtime_name=runtime_name,
            health=self.status(
                runtime_name
            ),
            checked_at=datetime.now(),
        )
