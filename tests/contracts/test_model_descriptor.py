from portable_ai.contracts.model_descriptor import ModelDescriptor


def test_model_descriptor_creation():
    model = ModelDescriptor(
        name="Qwen3.5-4B",
        version="1.0",
        format="GGUF",
        quantization="Q4_K_M",
        size_gb=2.7,
        license="Apache-2.0",
        capabilities=frozenset(
            {"text_generation", "vision"}
        ),
        minimum_ram_gb=8.0,
        checksum="abc123",
    )

    assert model.name == "Qwen3.5-4B"
    assert model.format == "GGUF"
    assert model.quantization == "Q4_K_M"
    assert "vision" in model.capabilities
    assert model.minimum_ram_gb == 8.0
