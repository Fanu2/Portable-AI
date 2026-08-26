from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ModelResource:
    """
    Describes a local model asset.
    """

    model_name: str

    path: Optional[str]

    size_gb: float

    format: str

    checksum: Optional[str] = None

    available: bool = True

    installed: bool = False

    minimum_ram_gb: Optional[float] = None
