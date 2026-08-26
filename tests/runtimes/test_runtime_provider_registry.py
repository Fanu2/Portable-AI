from portable_ai.runtimes.ollama_provider import (
    OllamaRuntimeProvider,
)
from portable_ai.runtimes.runtime_provider_registry import (
    RuntimeProviderRegistry,
)


class FakeClient:
    def health(self):
        return True


class FailingClient:
    def health(self):
        return False


def test_runtime_provider_registry_registers_provider():
    registry = RuntimeProviderRegistry()

    provider = OllamaRuntimeProvider(
        FakeClient()
    )

    registry.register(
        "ollama",
        provider,
    )

    assert registry.get("ollama") == provider
    assert len(registry.all()) == 1


def test_runtime_provider_registry_filters_available():
    registry = RuntimeProviderRegistry()

    available = OllamaRuntimeProvider(
        FakeClient()
    )

    unavailable = OllamaRuntimeProvider(
        FailingClient()
    )

    registry.register(
        "available",
        available,
    )

    registry.register(
        "unavailable",
        unavailable,
    )

    assert registry.available() == [
        available
    ]


def test_runtime_provider_registry_returns_named_providers():
    registry = RuntimeProviderRegistry()

    provider = OllamaRuntimeProvider(
        FakeClient()
    )

    registry.register(
        "ollama",
        provider,
    )

    assert registry.all_named() == {
        "ollama": provider
    }
