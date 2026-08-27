from portable_ai.assistant.assistant_factory import (
    AssistantFactory,
)

from portable_ai.assistant.assistant_service import (
    AssistantService,
)


class FakeRuntimeProvider:
    """
    Fake runtime provider.
    """

    def generate(
        self,
        prompt,
    ):
        return "response"


def test_assistant_factory_creates_default_assistant():

    factory = AssistantFactory()

    assistant = factory.create()

    assert isinstance(
        assistant,
        AssistantService,
    )


def test_assistant_factory_creates_runtime_backed_assistant():

    factory = AssistantFactory()

    runtime = FakeRuntimeProvider()

    assistant = factory.create(
        runtime
    )

    assert isinstance(
        assistant,
        AssistantService,
    )

    response = (
        assistant.generate_response()
    )

    # No prompt context yet,
    # so generation boundary exists
    assert response is None or isinstance(
        response,
        str,
    )
