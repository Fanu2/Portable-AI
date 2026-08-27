from portable_ai.assistant.session.session_contract import (
    AssistantSession,
)


def test_assistant_session_defaults():

    session = AssistantSession()

    assert (
        session.active
        is True
    )

    assert (
        session.conversation
        == []
    )


def test_assistant_session_stores_state():

    session = AssistantSession(
        conversation=[
            "hello"
        ],
        context={
            "mode": "test"
        },
    )

    assert (
        session.conversation[0]
        == "hello"
    )

    assert (
        session.context["mode"]
        == "test"
    )
