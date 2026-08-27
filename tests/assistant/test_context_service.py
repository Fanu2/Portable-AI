from portable_ai.assistant.context_service import (
    AssistantContextService,
)


def test_context_service_defaults():

    service = AssistantContextService()

    context = (
        service.get_context()
    )

    assert (
        context.conversation_id
        is None
    )


def test_context_service_sets_conversation():

    service = AssistantContextService()

    service.set_conversation_id(
        "chat-1"
    )

    context = (
        service.get_context()
    )

    assert (
        context.conversation_id
        == "chat-1"
    )


def test_context_service_sets_user_context():

    service = AssistantContextService()

    service.set_user_context(
        {
            "mode": "chat"
        }
    )

    context = (
        service.get_context()
    )

    assert (
        context.user_context["mode"]
        == "chat"
    )
