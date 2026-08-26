from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)

from portable_ai.services.capability_service import (
    CapabilityService,
)


def test_runtime_capabilities_are_registered():

    service = CapabilityService(
        CapabilityRegistry()
    )

    service.register_runtime_capabilities(
        "ollama",
        {
            "text_generation",
            "embeddings",
        },
    )

    names = [
        capability.name
        for capability in service.available()
    ]

    assert (
        "ollama:text_generation"
        in names
    )

    assert (
        "ollama:embeddings"
        in names
    )
