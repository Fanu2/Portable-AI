from portable_ai.models.model_registry import ModelRegistry
from portable_ai.services.model_catalog_service import ModelCatalogService


def test_model_catalog_loads_models():
    registry = ModelRegistry()

    service = ModelCatalogService(registry)

    models = service.load_catalog()

    assert len(models) == 2
    assert registry.get("Qwen3.5-4B") is not None
    assert registry.get("nomic-embed-text") is not None


def test_model_catalog_load_is_repeatable():
    registry = ModelRegistry()

    service = ModelCatalogService(registry)

    service.load_catalog()
    service.load_catalog()

    assert len(registry.all()) == 2


def test_model_catalog_models_support_capability_search():
    registry = ModelRegistry()

    service = ModelCatalogService(registry)
    service.load_catalog()

    embedding_models = registry.available_for_capability(
        "embeddings"
    )

    assert len(embedding_models) == 1
    assert embedding_models[0].name == "nomic-embed-text"
