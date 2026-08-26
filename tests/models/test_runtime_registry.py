from portable_ai.contracts.runtime_descriptor import RuntimeDescriptor
from portable_ai.models.runtime_registry import RuntimeRegistry


def test_runtime_registry_registers_and_retrieves_runtime():
    registry = RuntimeRegistry()

    runtime = RuntimeDescriptor(
        name="Ollama",
        version="0.32.1",
        available=True,
        capabilities=frozenset({"text_generation"}),
    )

    registry.register(runtime)

    assert registry.get("Ollama") == runtime
    assert len(registry.all()) == 1
    assert registry.available() == [runtime]


def test_runtime_registry_replaces_duplicate_runtime():
    registry = RuntimeRegistry()

    first = RuntimeDescriptor(
        name="Ollama",
        version="0.32.1",
        available=True,
        capabilities=frozenset({"text_generation"}),
    )

    second = RuntimeDescriptor(
        name="Ollama",
        version="0.33.0",
        available=True,
        capabilities=frozenset({"text_generation", "embeddings"}),
    )

    registry.register(first)
    registry.register(second)

    assert registry.get("Ollama") == second
    assert len(registry.all()) == 1


def test_runtime_registry_excludes_unavailable_runtimes():
    registry = RuntimeRegistry()

    available = RuntimeDescriptor(
        name="Ollama",
        version="0.32.1",
        available=True,
        capabilities=frozenset({"text_generation"}),
    )

    unavailable = RuntimeDescriptor(
        name="Jan",
        version=None,
        available=False,
        capabilities=frozenset(),
    )

    registry.register(available)
    registry.register(unavailable)

    assert registry.all() == [available, unavailable]
    assert registry.available() == [available]
