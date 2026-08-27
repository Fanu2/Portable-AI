from portable_ai.assistant.assistant_service import (
    AssistantService,
)


def test_assistant_foundation_has_no_execution_dependency():
    """
    Assistant foundation must operate
    without execution services.

    This protects the architecture boundary.
    """

    service = AssistantService()

    service.send_message(
        "hello"
    )

    history = (
        service.conversation_history()
    )

    assert len(history) == 1

    assert (
        history[0].content
        == "hello"
    )


def test_assistant_foundation_has_context_without_runtime():
    """
    Assistant context exists without
    runtime/model dependencies.
    """

    service = AssistantService()

    context = (
        service.context()
    )

    prompt_context = (
        service.prompt_context()
    )

    assert context is not None

    assert prompt_context is not None


def test_assistant_foundation_clear_isolated_state():
    """
    Clearing assistant state should not
    require any execution layer.
    """

    service = AssistantService()

    service.send_message(
        "temporary"
    )

    service.clear()

    assert (
        service.conversation_history()
        == []
    )
