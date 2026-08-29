from portable_ai.models.runtime_health import (
    RuntimeHealth,
)

from portable_ai.models.runtime_readiness import (
    RuntimeReadiness,
)


class RuntimeReadinessService:
    """
    Determines whether a runtime is ready
    for execution.

    Uses runtime health as the initial
    readiness boundary.
    """

    def __init__(
        self,
        health_service,
    ) -> None:

        self._health_service = (
            health_service
        )

    def check(
        self,
        runtime_name: str,
    ) -> RuntimeReadiness:

        health = (
            self._health_service.status(
                runtime_name
            )
        )

        ready = (
            health == RuntimeHealth.ONLINE
        )

        reason = (
            "runtime online"
            if ready
            else "runtime not ready"
        )

        return RuntimeReadiness(
            runtime_name=runtime_name,
            health=health,
            ready=ready,
            reason=reason,
        )
