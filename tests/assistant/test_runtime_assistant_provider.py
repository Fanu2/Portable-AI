from portable_ai.assistant.providers.runtime_assistant_provider import (
    RuntimeAssistantProvider,
)


class FakeRuntimeProvider:
    """
    Fake runtime provider for testing.
    """

    def __init__(
        self,
    ) -> None:

        self.received_prompt = None

    def generate(
        self,
        prompt,
    ):

        self.received_prompt = prompt

        return "runtime response"


def test_runtime_assistant_provider_generates_response():

    runtime = FakeRuntimeProvider()

    provider = RuntimeAssistantProvider(
        runtime
    )

    response = provider.generate(
        "hello"
    )

    assert response == (
        "runtime response"
    )

    assert runtime.received_prompt == (
        "hello"
    )
