from portable_ai.models.model_registry import ModelRegistry
from portable_ai.services.runtime_model_importer import (
    RuntimeModelImporter,
)
from portable_ai.services.runtime_sync_service import (
    RuntimeSyncService,
)


def test_runtime_sync_service_syncs_models():
    registry = ModelRegistry()

    service = RuntimeSyncService(
        RuntimeModelImporter(registry)
    )

    models = service.sync(
        "Ollama",
        ["qwen3:4b"],
    )

    assert len(models) == 1
    assert registry.get("qwen3:4b") is not None
