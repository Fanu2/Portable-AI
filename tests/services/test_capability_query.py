from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)

from portable_ai.services.capability_service import (
    CapabilityService,
)


def test_capability_query_by_runtime():

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

    capabilities = service.for_runtime(
        "ollama"
    )

    names = [
        capability.name
        for capability in capabilities
    ]

    assert (
        "ollama:text_generation"
        in names
    )

    assert (
        "ollama:embeddings"
        in names
    )


def test_capability_query_unknown_runtime():

    service = CapabilityService(
        CapabilityRegistry()
    )

    assert (
        service.for_runtime("missing")
        == []
    )
