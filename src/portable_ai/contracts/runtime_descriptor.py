from dataclasses import dataclass
from typing import FrozenSet, Optional


@dataclass(frozen=True)
class RuntimeDescriptor:
    """
    Describes an AI runtime discovered on the host system.
    """

    name: str
    version: Optional[str]
    available: bool
    capabilities: FrozenSet[str]
    executable: Optional[str] = None
    endpoint: Optional[str] = None
