from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.assistant.response_generation_service import (
    ResponseGenerationService,
)

from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)

from portable_ai.services.assistant_ui_service import (
    AssistantUIService,
)


class FakeResponseProvider(
    AssistantProvider
):
    """
    Fake assistant provider.

    Confirms the lifecycle reaches
    the provider boundary.
    """

    def generate(
        self,
        context,
    ):

        assert (
            context.conversation
            is not None
        )

        return "assistant response"


def test_assistant_response_lifecycle():

    assistant = AssistantService(
        response_generation_service=(
            ResponseGenerationService(
                FakeResponseProvider()
            )
        )
    )

    ui = AssistantUIService(
        assistant
    )

    history = ui.send_message(
        "hello"
    )

    assert history is not None

    assert (
        history[0].content
        == "hello"
    )

    response = (
        ui.generate_response()
    )

    assert (
        response
        == "assistant response"
    )
