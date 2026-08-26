from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.contracts.runtime_executor import (
    RuntimeExecutor,
)

from portable_ai.models.executor_registry import (
    ExecutorRegistry,
)

from portable_ai.services.execution_service import (
    ExecutionService,
)

from portable_ai.services.execution_result_validator import (
    ExecutionResultValidator,
)


class FailingExecutor(RuntimeExecutor):

    def execute(
        self,
        request,
    ):
        raise RuntimeError(
            "runtime failed"
        )


def test_execution_service_handles_executor_failure():

    registry = ExecutorRegistry()

    registry.register(
        "broken",
        FailingExecutor(),
    )

    service = ExecutionService(
        registry,
        ExecutionResultValidator(),
    )

    result = service.execute(
        "broken",
        ExecutionRequest(
            runtime="broken",
            model="test",
            prompt="hello",
        ),
    )

    assert result is None
