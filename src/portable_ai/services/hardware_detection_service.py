import os
import shutil

from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)


class HardwareDetectionService:
    """
    Detects local machine hardware information.
    """

    def detect(
        self,
    ) -> HardwareInfo:

        return HardwareInfo(
            cpu_cores=self._detect_cpu_cores(),
            ram_gb=self._detect_memory(),
            storage_gb=self._detect_storage(),
        )

    def _detect_cpu_cores(
        self,
    ) -> int:

        return os.cpu_count() or 1

    def _detect_memory(
        self,
    ) -> float:

        try:
            import psutil

            memory = psutil.virtual_memory()

            return round(
                memory.total / (1024 ** 3),
                2,
            )

        except ImportError:
            pass

        except Exception:
            pass

        return self._detect_memory_linux()

    def _detect_memory_linux(
        self,
    ) -> float:

        try:
            with open(
                "/proc/meminfo",
                "r",
                encoding="utf-8",
            ) as file:

                for line in file:

                    if line.startswith(
                        "MemTotal:"
                    ):

                        kb = int(
                            line.split()[1]
                        )

                        return round(
                            kb / (1024 ** 2),
                            2,
                        )

        except Exception:
            pass

        return 0.0

    def _detect_storage(
        self,
    ) -> float:

        try:
            usage = shutil.disk_usage(
                "/"
            )

            return round(
                usage.total / (1024 ** 3),
                2,
            )

        except OSError:
            return 0.0
