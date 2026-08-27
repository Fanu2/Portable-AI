from portable_ai.assistant.assistant_service import (
    AssistantService,
)


def test_assistant_service_updates_prompt_context():

    service = AssistantService()

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


def test_assistant_service_exposes_prompt_context():

    service = AssistantService()

    context = (
        service.prompt_context()
    )

    assert (
        context
        is not None
    )


def test_assistant_service_exposes_assistant_context():

    service = AssistantService()

    context = (
        service.context()
    )

    assert (
        context
        is not None
    )


def test_assistant_service_session_exposes_workspace_context():

    service = AssistantService()

    session = (
        service.session()
    )

    assert (
        session.workspace
        is not None
    )

    assert (
        service.prompt_context()
        .workspace_context
        is not None
    )
