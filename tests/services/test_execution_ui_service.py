from portable_ai.services.execution_ui_service import (
    ExecutionUIService,
)


class FakeActiveExecution:

    def __init__(
        self,
    ):

        self.prompt = None

    def execute(
        self,
        prompt,
    ):

        self.prompt = prompt

        return "response"


def test_execution_ui_service_forwards_prompt():

    active = FakeActiveExecution()

    service = ExecutionUIService(
        active
    )

    result = service.execute(
        "Hello AI"
    )

    assert result == "response"

    assert (
        active.prompt
        == "Hello AI"
    )


def test_execution_ui_service_rejects_empty_prompt():

    active = FakeActiveExecution()

    service = ExecutionUIService(
        active
    )

    assert (
        service.execute("")
        is None
    )
