from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.services.assistant_ui_service import (
    AssistantUIService,
)


def test_assistant_ui_exposes_prompt_context():

    service = AssistantUIService(
        AssistantService()
    )

    service.send_message(
        "hello"
    )

    context = (
        service.prompt_context()
    )

    assert (
        context.conversation
        is not None
    )

    assert (
        context.conversation[0].content
        == "hello"
    )
