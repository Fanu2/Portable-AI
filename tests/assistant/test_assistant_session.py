from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.assistant.session.session_contract import (
    AssistantSession,
)


def test_assistant_service_exposes_session():

    service = AssistantService()

    session = (
        service.session()
    )

    assert isinstance(
        session,
        AssistantSession,
    )

    assert (
        session.active
        is True
    )

    assert (
        session.conversation
        == []
    )


def test_assistant_service_session_tracks_message():

    service = AssistantService()

    service.send_message(
        "hello"
    )

    session = (
        service.session()
    )

    assert len(
        session.conversation
    ) == 1

    assert (
        session.conversation[0].content
        == "hello"
    )


def test_assistant_service_clear_resets_session():

    service = AssistantService()

    service.send_message(
        "hello"
    )

    service.clear()

    session = (
        service.session()
    )

    assert (
        session.conversation
        == []
    )

    assert (
        session.active
        is True
    )
