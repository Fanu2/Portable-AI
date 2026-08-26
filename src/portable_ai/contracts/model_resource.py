from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ModelResource:
    """
    Describes a local model asset.
    """

    model_name: str

    path: str

    size_gb: float

    format: str

    checksum: Optional[str] = None

    available: bool = True
