from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.services.execution_adapter_service import (
    ExecutionAdapterService,
)


class FakeExecutionService:
    """
    Fake execution engine for adapter testing.
    """

    def __init__(
        self,
    ):

        self.received = None

    def execute(
        self,
        request,
    ):

        self.received = request

        return "result"


def test_execution_adapter_forwards_request():

    execution = FakeExecutionService()

    service = ExecutionAdapterService(
        execution
    )

    request = ExecutionRequest(
        runtime="ollama",
        model="Qwen3.5-4B",
        prompt="Hello",
    )

    result = service.execute(
        request
    )

    assert result == "result"

    assert (
        execution.received
        == request
    )


def test_execution_adapter_handles_none():

    execution = FakeExecutionService()

    service = ExecutionAdapterService(
        execution
    )

    result = service.execute(
        None
    )

    assert result is None
