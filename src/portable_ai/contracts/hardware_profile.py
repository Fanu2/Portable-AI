from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class HardwareProfile:
    """
    Describes the host machine capabilities.
    """

    operating_system: str
    architecture: str
    cpu: str
    ram_gb: float
    gpu: Optional[str] = None
    vram_gb: Optional[float] = None
    storage_free_gb: Optional[float] = None
