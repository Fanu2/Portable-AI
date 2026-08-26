from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class HardwareInfo:
    """
    Describes local machine capabilities.
    """

    cpu_cores: int

    ram_gb: float

    gpu_name: Optional[str] = None

    gpu_memory_gb: Optional[float] = None

    storage_gb: Optional[float] = None
