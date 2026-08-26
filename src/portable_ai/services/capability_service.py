from portable_ai.models.capability_descriptor import (
    CapabilityDescriptor,
)

from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)


class CapabilityService:
    """
    Provides capability information.
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

    def register_runtime_capabilities(
        self,
        runtime_name: str,
        capabilities: set[str],
    ) -> None:
        for capability in capabilities:
            self.register(
                f"{runtime_name}:{capability}",
                f"{runtime_name} supports {capability}",
            )

    def for_runtime(
        self,
        runtime_name: str,
    ):
        prefix = (
            runtime_name
            + ":"
        )

        return [
            capability
            for capability in self._registry.all()
            if capability.name.startswith(prefix)
        ]
