from portable_ai.assistant.assistant_service import (
    AssistantService,
)


def test_assistant_service_stores_message():

    service = AssistantService()

    service.send_message(
        "Hello"
    )

    history = (
        service.conversation_history()
    )

    assert len(history) == 1

    assert (
        history[0].content
        == "Hello"
    )


def test_assistant_service_exposes_context():

    service = AssistantService()

    context = (
        service.context()
    )

    assert context is not None


def test_assistant_service_clears_history():

    service = AssistantService()

    service.send_message(
        "Hello"
    )

    service.clear()

    assert (
        service.conversation_history()
        == []
    )
