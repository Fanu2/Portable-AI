from portable_ai.retrieval.retrieval_registry import (
    RetrievalRegistry,
)


class FakeProvider:
    pass


def test_retrieval_registry_registers_provider():

    registry = RetrievalRegistry()

    provider = FakeProvider()

    registry.register(
        "memory",
        provider,
    )

    assert (
        registry.get("memory")
        == provider
    )


def test_retrieval_registry_lists_names():

    registry = RetrievalRegistry()

    registry.register(
        "memory",
        FakeProvider(),
    )

    assert (
        "memory"
        in registry.names()
    )
