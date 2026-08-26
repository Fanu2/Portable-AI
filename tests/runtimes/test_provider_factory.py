from portable_ai.contracts.runtime_descriptor import (
    RuntimeDescriptor,
)
from portable_ai.runtimes.provider_factory import (
    ProviderFactory,
)


def test_provider_factory_creates_ollama_provider():
    descriptor = RuntimeDescriptor(
        name="Ollama",
        version=None,
        available=True,
        capabilities=frozenset(
            {"text_generation"}
        ),
        executable="/usr/bin/ollama",
    )

    provider = ProviderFactory().create(
        descriptor
    )

    assert provider is not None
    assert "text_generation" in provider.capabilities()
