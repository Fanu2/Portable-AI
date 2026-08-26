from portable_ai.models.capability_descriptor import (
    CapabilityDescriptor,
)


class CapabilityRegistry:
    """
    Stores available capabilities.
    """

    def __init__(self) -> None:
        self._capabilities = {}

    def register(
        self,
        capability: CapabilityDescriptor,
    ) -> None:
        self._capabilities[
            capability.name
        ] = capability

    def get(
        self,
        name: str,
    ):
        return self._capabilities.get(
            name
        )

    def all(self):
        return list(
            self._capabilities.values()
        )
