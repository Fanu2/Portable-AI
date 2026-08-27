from portable_ai.contracts.assistant_context import (
    AssistantContext,
)


def test_assistant_context_defaults():

    context = AssistantContext()

    assert (
        context.conversation_id
        is None
    )

    assert (
        context.user_context
        is None
    )


def test_assistant_context_stores_state():

    context = AssistantContext(
        conversation_id="test-1",
        user_context={
            "mode": "chat"
        },
    )

    assert (
        context.conversation_id
        == "test-1"
    )

    assert (
        context.user_context["mode"]
        == "chat"
    )
