from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.services.runtime_model_importer import (
    RuntimeModelImporter,
)


def test_runtime_model_importer_registers_models():

    registry = ModelRegistry()

    importer = RuntimeModelImporter(
        registry
    )

    models = importer.import_models(
        "Ollama",
        [
            "qwen3:4b",
            "nomic-embed-text",
        ],
    )

    assert len(models) == 2

    assert registry.get(
        "qwen3:4b"
    ) is not None

    assert registry.get(
        "nomic-embed-text"
    ) is not None

    assert (
        models[0].source_runtime
        == "Ollama"
    )


def test_runtime_model_importer_preserves_existing_metadata():

    registry = ModelRegistry()

    existing = ModelDescriptor(
        name="qwen3:4b",
        version="catalog",
        format="GGUF",
        quantization="Q4_K_M",
        size_gb=2.7,
        license="Apache-2.0",
        capabilities=frozenset(
            {
                "text_generation",
            }
        ),
        minimum_ram_gb=4.0,
        checksum="abc123",
    )

    registry.register(
        existing
    )

    importer = RuntimeModelImporter(
        registry
    )

    models = importer.import_models(
        "ollama",
        [
            "qwen3:4b",
        ],
    )

    imported = models[0]

    assert (
        imported.version
        == "catalog"
    )

    assert (
        imported.format
        == "GGUF"
    )

    assert (
        imported.quantization
        == "Q4_K_M"
    )

    assert (
        imported.size_gb
        == 2.7
    )

    assert (
        imported.license
        == "Apache-2.0"
    )

    assert (
        imported.capabilities
        == frozenset(
            {
                "text_generation",
            }
        )
    )

    assert (
        imported.minimum_ram_gb
        == 4.0
    )

    assert (
        imported.checksum
        == "abc123"
    )

    assert (
        imported.source_runtime
        == "ollama"
    )
