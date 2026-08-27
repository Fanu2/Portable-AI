from portable_ai.assistant.providers.provider_factory import (
    ProviderFactory,
)

from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)


class FakeProvider(
    AssistantProvider
):

    def generate(
        self,
        context,
    ):

        return "response"


def test_provider_factory_returns_provider():

    provider = FakeProvider()

    result = ProviderFactory().create(
        provider
    )

    assert (
        result
        is provider
    )


def test_provider_factory_without_provider():

    result = ProviderFactory().create()

    assert (
        result
        is None
    )
