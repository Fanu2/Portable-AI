from portable_ai.services.capability_service import (
    CapabilityService,
)

from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)


def test_capability_service_registers():

    service = CapabilityService(
        CapabilityRegistry()
    )

    service.register(
        "text_generation",
        "Generate text",
    )

    capabilities = service.available()

    assert len(capabilities) == 1

    assert (
        capabilities[0].name
        == "text_generation"
    )
