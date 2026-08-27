from portable_ai.assistant.assistant_status_service import (
    AssistantStatusService,
)


def test_status_without_provider():

    service = AssistantStatusService()

    status = service.health()

    assert status["available"] is False


def test_status_with_provider():

    service = AssistantStatusService(
        object()
    )

    status = service.health()

    assert status["available"] is True
