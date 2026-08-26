from dataclasses import dataclass


@dataclass(frozen=True)
class CapabilityDescriptor:
    """
    Describes a runtime capability.
    """

    name: str

    description: str
