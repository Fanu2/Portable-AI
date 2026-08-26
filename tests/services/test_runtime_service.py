from portable_ai.runtimes.runtime_provider_registry import (
    RuntimeProviderRegistry,
)
from portable_ai.services.runtime_service import (
    RuntimeService,
)


class FakeRuntime:

    def generate(self, prompt, **kwargs):
        return "response"

    def embed(self, text):
        return [
            0.1,
            0.2,
        ]


def test_runtime_service_returns_missing_runtime_as_none():
    registry = RuntimeProviderRegistry()

    service = RuntimeService(
        registry
    )

    assert service.get_runtime(
        "missing"
    ) is None


def test_runtime_service_generates_response():
    registry = RuntimeProviderRegistry()

    registry.register(
        "ollama",
        FakeRuntime(),
    )

    service = RuntimeService(
        registry
    )

    result = service.generate(
        "ollama",
        "hello",
    )

    assert result == "response"


def test_runtime_service_creates_embeddings():
    registry = RuntimeProviderRegistry()

    registry.register(
        "ollama",
        FakeRuntime(),
    )

    service = RuntimeService(
        registry
    )

    result = service.embed(
        "ollama",
        "hello",
    )

    assert result == [
        0.1,
        0.2,
    ]
