from portable_ai.contracts.hardware_detector import HardwareDetector
from portable_ai.contracts.hardware_profile import HardwareProfile


class HardwareService:
    """
    Application service for hardware information.
    """

    def __init__(
        self,
        detector: HardwareDetector,
    ) -> None:
        self._detector = detector

    def profile(self) -> HardwareProfile:
        return self._detector.detect()
