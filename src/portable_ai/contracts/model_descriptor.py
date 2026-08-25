from dataclasses import dataclass
from typing import FrozenSet, Optional


@dataclass(frozen=True)
class ModelDescriptor:
    """
    Describes a local AI model asset.
    """

    name: str
    version: str
    format: str
    quantization: Optional[str]
    size_gb: float
    license: str
    capabilities: FrozenSet[str]
    minimum_ram_gb: Optional[float] = None
    checksum: Optional[str] = None
    
