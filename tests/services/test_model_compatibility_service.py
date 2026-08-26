from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.services.model_compatibility_service import (
    ModelCompatibilityService,
)


def test_model_capability_matching():

    registry = ModelRegistry()

    registry.register(
        ModelDescriptor(
            name="Qwen3.5-4B",
            version="1.0",
            format="GGUF",
            quantization="Q4_K_M",
            size_gb=2.7,
            license="Apache-2.0",
            capabilities=frozenset(
                {"text_generation"}
            ),
        )
    )

    service = ModelCompatibilityService(
        registry
    )

    assert service.supports(
        "Qwen3.5-4B",
        "text_generation",
    )

    assert not service.supports(
        "Qwen3.5-4B",
        "vision",
    )
