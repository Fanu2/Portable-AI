from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class CapabilityDescriptor:
    """
    Describes capabilities provided by a model or runtime.
    """

    capabilities: FrozenSet[str]

    def supports(self, capability: str) -> bool:
        return capability in self.capabilities
