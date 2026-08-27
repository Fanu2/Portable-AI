from portable_ai.assistant.providers.provider_registry import (
    ProviderRegistry,
)


class FakeProvider:
    """
    Fake provider for registry testing.
    """

    pass


def test_provider_registry_registers_provider():

    registry = ProviderRegistry()

    provider = FakeProvider()

    registry.register(
        "fake",
        provider,
    )

    assert (
        registry.get("fake")
        is provider
    )


def test_provider_registry_lists_provider_names():

    registry = ProviderRegistry()

    registry.register(
        "fake",
        FakeProvider(),
    )

    assert (
        "fake"
        in registry.names()
    )
