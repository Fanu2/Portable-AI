from portable_ai.contracts.runtime_descriptor import RuntimeDescriptor


def test_runtime_descriptor_creation():
    runtime = RuntimeDescriptor(
        name="Ollama",
        version="0.32.1",
        available=True,
        capabilities=frozenset(
            {"text_generation", "embeddings"}
        ),
        executable="/usr/local/bin/ollama",
        endpoint="http://127.0.0.1:11434",
    )

    assert runtime.name == "Ollama"
    assert runtime.version == "0.32.1"
    assert runtime.available
    assert "embeddings" in runtime.capabilities
    assert runtime.endpoint == "http://127.0.0.1:11434"
