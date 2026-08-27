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


class FakeGenerator(
    AssistantProvider
):
    """
    Fake assistant provider.

    Uses the AssistantProvider contract.
    """

    def generate(
        self,
        context,
    ):

        return "assistant reply"


def test_assistant_ui_generates_response():

    assistant = AssistantService(
        response_generation_service=(
            ResponseGenerationService(
                FakeGenerator()
            )
        )
    )

    ui = AssistantUIService(
        assistant
    )

    ui.send_message(
        "hello"
    )

    result = (
        ui.generate_response()
    )

    assert (
        result
        == "assistant reply"
    )
