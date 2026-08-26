from portable_ai.models.catalog.runtime_catalog import RUNTIME_DEFINITIONS


def test_runtime_catalog_contains_known_runtimes():
    names = {
        runtime.name
        for runtime in RUNTIME_DEFINITIONS
    }

    assert "Ollama" in names
    assert "llama.cpp" in names
    assert "LM Studio" in names
    assert "Jan" in names
