from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)

from portable_ai.services.capability_service import (
    CapabilityService,
)


def create_capability_service():

    registry = CapabilityRegistry()

    service = CapabilityService(
        registry
    )

    service.register(
        "text_generation",
        "Generate text responses",
    )

    service.register(
        "embeddings",
        "Generate vector embeddings",
    )

    return service
