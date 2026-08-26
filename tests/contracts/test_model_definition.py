from portable_ai.contracts.model_definition import ModelDefinition


def test_model_definition_creation():
    model = ModelDefinition(
        name="Qwen3.5-4B",
        format="GGUF",
        capabilities=frozenset(
            {"text_generation"}
        ),
        default_quantization="Q4_K_M",
        license="Apache-2.0",
    )

    assert model.name == "Qwen3.5-4B"
    assert model.format == "GGUF"
    assert "text_generation" in model.capabilities
    assert model.default_quantization == "Q4_K_M"
