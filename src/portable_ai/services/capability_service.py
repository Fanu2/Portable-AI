from portable_ai.models.capability_descriptor import (
    CapabilityDescriptor,
)

from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)


class CapabilityService:
    """
    Provides runtime capability information.
    """

    def __init__(
        self,
        registry: CapabilityRegistry,
    ) -> None:
        self._registry = registry

    def register(
        self,
        name: str,
        description: str,
    ) -> None:
        self._registry.register(
            CapabilityDescriptor(
                name=name,
                description=description,
            )
        )

    def available(self):
        return self._registry.all()
