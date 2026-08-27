from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.services.assistant_ui_service import (
    AssistantUIService,
)


def test_assistant_lifecycle_stores_conversation():
    """
    Validate complete assistant lifecycle.

    Message should travel:

        UI boundary
            |
            ▼
        Assistant service
            |
            ▼
        Conversation storage
    """

    assistant = AssistantService()

    ui = AssistantUIService(
        assistant
    )

    result = ui.send_message(
        "hello assistant"
    )

    assert result is not None

    assert (
        len(result)
        == 1
    )

    assert (
        result[0].sender
        == "user"
    )

    assert (
        result[0].content
        == "hello assistant"
    )


def test_assistant_lifecycle_exposes_context():

    assistant = AssistantService()

    context = (
        assistant.context()
    )

    assert context is not None


def test_assistant_lifecycle_clear():

    assistant = AssistantService()

    ui = AssistantUIService(
        assistant
    )

    ui.send_message(
        "temporary"
    )

    assistant.clear()

    assert (
        assistant.conversation_history()
        == []
    )
