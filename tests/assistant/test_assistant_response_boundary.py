from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.assistant.response_generation_service import (
    ResponseGenerationService,
)

from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)


class FakeGenerator(
    AssistantProvider
):
    """
    Fake assistant provider.

    Confirms AssistantService uses
    the response generation boundary
    through AssistantProvider.
    """

    def generate(
        self,
        context,
    ):

        return "assistant reply"


def test_assistant_service_generates_response():

    service = AssistantService(
        response_generation_service=(
            ResponseGenerationService(
                FakeGenerator()
            )
        )
    )

    service.send_message(
        "hello"
    )

    result = (
        service.generate_response()
    )

    assert (
        result
        == "assistant reply"
    )
