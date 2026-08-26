from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.services.model_selection_service import (
    ModelSelectionService,
)


def create_model(
    name,
    capabilities,
):
    return ModelDescriptor(
        name=name,
        version="1.0",
        format="GGUF",
        quantization="Q4_K_M",
        size_gb=2.7,
        license="Apache-2.0",
        capabilities=frozenset(
            capabilities
        ),
    )


def test_select_model_for_capability():

    registry = ModelRegistry()

    registry.register(
        create_model(
            "Qwen3.5-4B",
            {
                "text_generation",
            },
        )
    )

    service = ModelSelectionService(
        registry
    )

    model = service.select_for_capability(
        "text_generation"
    )

    assert model is not None

    assert (
        model.name
        == "Qwen3.5-4B"
    )


def test_select_unknown_capability():

    registry = ModelRegistry()

    service = ModelSelectionService(
        registry
    )

    assert (
        service.select_for_capability(
            "vision"
        )
        is None
    )
