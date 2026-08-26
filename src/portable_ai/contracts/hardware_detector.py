from abc import ABC, abstractmethod

from portable_ai.contracts.hardware_profile import HardwareProfile


class HardwareDetector(ABC):
    """
    Abstract interface for detecting host hardware.
    """

    @abstractmethod
    def detect(self) -> HardwareProfile:
        """
        Detect and return hardware profile.
        """
        raise NotImplementedError
