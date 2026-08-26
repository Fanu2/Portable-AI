from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class RuntimeDefinition:
    """
    Static definition used to discover an AI runtime.
    """

    name: str
    executable_names: tuple[str, ...]
    capabilities: FrozenSet[str]
