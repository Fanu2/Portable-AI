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
    ) -> None:

        self.executor_name = None
        self.received = None

    def execute(
        self,
        executor_name,
        request,
    ):

        self.executor_name = (
            executor_name
        )

        self.received = request

        return "result"


def test_execution_adapter_forwards_request():

    execution = FakeExecutionService()

    service = ExecutionAdapterService(
        execution
    )

    request = ExecutionRequest(
        runtime="ollama",
        model="qwen3:4b",
        prompt="Hello",
    )

    result = service.execute(
        request
    )

    assert result == "result"

    assert execution.executor_name == "ollama"

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
