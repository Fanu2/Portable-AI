from portable_ai.contracts.runtime_definition import RuntimeDefinition


def test_runtime_definition_creation():
    definition = RuntimeDefinition(
        name="Ollama",
        executable_names=("ollama",),
        capabilities=frozenset({"text_generation", "embeddings"}),
    )

    assert definition.name == "Ollama"
    assert definition.executable_names == ("ollama",)
    assert "embeddings" in definition.capabilities
