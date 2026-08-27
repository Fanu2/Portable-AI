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


def test_assistant_provider_contract():

    provider = FakeProvider()

    result = provider.generate(
        "context"
    )

    assert (
        result
        == "response"
    )
