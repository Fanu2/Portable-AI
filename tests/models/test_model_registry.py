from portable_ai.contracts.model_descriptor import ModelDescriptor
from portable_ai.models.model_registry import ModelRegistry


def create_model(
    name: str,
    capabilities: frozenset[str],
) -> ModelDescriptor:
    return ModelDescriptor(
        name=name,
        version="1.0",
        format="GGUF",
        quantization="Q4_K_M",
        size_gb=2.7,
        license="Apache-2.0",
        capabilities=capabilities,
    )


def test_model_registry_registers_and_retrieves_model():
    registry = ModelRegistry()

    model = create_model(
        "Qwen3.5-4B",
        frozenset({"text_generation"}),
    )

    registry.register(model)

    assert registry.get("Qwen3.5-4B") == model
    assert len(registry.all()) == 1


def test_model_registry_replaces_duplicate_model():
    registry = ModelRegistry()

    first = create_model(
        "Qwen3.5-4B",
        frozenset({"text_generation"}),
    )

    second = create_model(
        "Qwen3.5-4B",
        frozenset({"text_generation", "vision"}),
    )

    registry.register(first)
    registry.register(second)

    assert registry.get("Qwen3.5-4B") == second
    assert len(registry.all()) == 1


def test_model_registry_filters_by_capability():
    registry = ModelRegistry()

    text_model = create_model(
        "Qwen3.5-4B",
        frozenset({"text_generation"}),
    )

    vision_model = create_model(
        "Gemma-12B",
        frozenset({"text_generation", "vision"}),
    )

    registry.register(text_model)
    registry.register(vision_model)

    results = registry.available_for_capability("vision")

    assert results == [vision_model]
