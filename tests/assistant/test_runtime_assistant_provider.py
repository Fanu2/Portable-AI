from portable_ai.assistant.providers.runtime_assistant_provider import (
    RuntimeAssistantProvider,
)

from portable_ai.contracts.runtime_provider import (
    RuntimeProvider,
)


class FakeRuntimeProvider(
    RuntimeProvider
):
    """
    Fake runtime provider.

    Confirms adapter delegates
    generation correctly.
    """

    def discover(self):
        return {}

    def capabilities(self):
        return set()

    def metadata(self):
        return {}

    def load_model(
        self,
        model_id,
    ):
        return True

    def unload_model(
        self,
        model_id,
    ):
        return True

    def generate(
        self,
        prompt,
        **kwargs,
    ):

        assert (
            prompt
            == "hello"
        )

        return "response"

    def embed(
        self,
        text,
    ):
        return []

    def health(self):
        return True


def test_runtime_assistant_provider_delegates_generation():

    provider = RuntimeAssistantProvider(
        FakeRuntimeProvider()
    )

    result = provider.generate(
        "hello"
    )

    assert (
        result
        == "response"
    )
