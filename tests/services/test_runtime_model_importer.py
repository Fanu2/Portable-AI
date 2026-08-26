from portable_ai.models.model_registry import ModelRegistry
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

    assert registry.get("qwen3:4b") is not None
    assert registry.get("nomic-embed-text") is not None

    assert models[0].source_runtime == "Ollama"
