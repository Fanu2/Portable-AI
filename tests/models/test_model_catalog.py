from portable_ai.models.catalog.model_catalog import MODEL_DEFINITIONS


def test_model_catalog_contains_known_models():
    names = {
        model.name
        for model in MODEL_DEFINITIONS
    }

    assert "Qwen3.5-4B" in names
    assert "nomic-embed-text" in names
