from portable_ai.runtimes.ollama_provider import (
    OllamaRuntimeProvider,
)


class FakeClient:
    def health(self):
        return True

    def generate(self, prompt, **kwargs):
        return "response"

    def embed(self, text):
        return [0.1, 0.2]


def test_ollama_provider_health():
    provider = OllamaRuntimeProvider(
        FakeClient()
    )

    assert provider.health()


def test_ollama_provider_capabilities():
    provider = OllamaRuntimeProvider(
        FakeClient()
    )

    capabilities = provider.capabilities()

    assert "text_generation" in capabilities
    assert "embeddings" in capabilities


def test_ollama_provider_generate_delegates():
    provider = OllamaRuntimeProvider(
        FakeClient()
    )

    result = provider.generate(
        "hello"
    )

    assert result == "response"


def test_ollama_provider_embed_delegates():
    provider = OllamaRuntimeProvider(
        FakeClient()
    )

    result = provider.embed(
        "hello"
    )

    assert result == [
        0.1,
        0.2,
    ]
