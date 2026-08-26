from dataclasses import dataclass
from typing import FrozenSet, Optional


@dataclass(frozen=True)
class ModelDefinition:
    """
    Static definition of a model available for discovery.
    """

    name: str
    format: str
    capabilities: FrozenSet[str]
    default_quantization: Optional[str] = None
    license: Optional[str] = None
