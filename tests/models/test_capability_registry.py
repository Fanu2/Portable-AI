from portable_ai.models.capability_descriptor import (
    CapabilityDescriptor,
)

from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)


def test_capability_registry_registers():

    registry = CapabilityRegistry()

    capability = CapabilityDescriptor(
        name="text_generation",
        description="Generate text",
    )

    registry.register(
        capability
    )

    assert (
        registry.get(
            "text_generation"
        )
        == capability
    )


def test_capability_registry_lists():

    registry = CapabilityRegistry()

    registry.register(
        CapabilityDescriptor(
            name="embeddings",
            description="Create vectors",
        )
    )

    assert len(
        registry.all()
    ) == 1
