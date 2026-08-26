from abc import ABC, abstractmethod

from portable_ai.models.runtime_health_snapshot import (
    RuntimeHealthSnapshot,
)


class RuntimeMonitor(ABC):
    """
    Interface for runtime monitoring.
    """

    @abstractmethod
    def check(
        self,
        runtime_name: str,
    ) -> RuntimeHealthSnapshot:
        """
        Check runtime health.
        """
        pass
