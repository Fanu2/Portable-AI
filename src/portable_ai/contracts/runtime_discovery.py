from abc import ABC, abstractmethod

from portable_ai.contracts.runtime_descriptor import RuntimeDescriptor


class RuntimeDiscovery(ABC):
    """
    Abstract interface for discovering AI runtimes on the host.
    """

    @abstractmethod
    def discover(self) -> list[RuntimeDescriptor]:
        """
        Discover available AI runtimes.
        """
        raise NotImplementedError
