from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.services.assistant_ui_service import (
    AssistantUIService,
)


def test_assistant_ui_forwards_message():
    """
    Verify UI assistant boundary forwards
    messages into AssistantService.
    """

    assistant = AssistantService()

    service = AssistantUIService(
        assistant
    )

    result = service.send_message(
        "Hello"
    )

    assert result is not None

    assert (
        result[0].content
        == "Hello"
    )

    assert (
        result[0].sender
        == "user"
    )


def test_assistant_ui_rejects_empty_message():
    """
    Empty messages should not create
    conversation entries.
    """

    service = AssistantUIService(
        AssistantService()
    )

    assert (
        service.send_message("")
        is None
    )
