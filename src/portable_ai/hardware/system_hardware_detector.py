import os
import platform

from portable_ai.contracts.hardware_profile import HardwareProfile
from portable_ai.contracts.hardware_detector import HardwareDetector


class SystemHardwareDetector(HardwareDetector):
    """
    Detects basic host hardware information.
    """

    def detect(self) -> HardwareProfile:
        return HardwareProfile(
            operating_system=platform.system(),
            architecture=platform.machine(),
            cpu=platform.processor(),
            ram_gb=self._ram_gb(),
            storage_free_gb=self._storage_free_gb(),
        )

    def _ram_gb(self) -> float:
        pages = os.sysconf("SC_PHYS_PAGES")
        page_size = os.sysconf("SC_PAGE_SIZE")

        return round(
            (pages * page_size) / (1024 ** 3),
            2,
        )

    def _storage_free_gb(self) -> float:
        stat = os.statvfs(".")

        return round(
            (stat.f_bavail * stat.f_frsize) / (1024 ** 3),
            2,
        )
