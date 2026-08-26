from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.contracts.execution_result import (
    ExecutionResult,
)

from portable_ai.contracts.runtime_executor import (
    RuntimeExecutor,
)


class FakeRuntimeExecutor(
    RuntimeExecutor
):
    """
    Test execution implementation.
    """

    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:

        return ExecutionResult(
            runtime=request.runtime,
            model=request.model,
            response="fake response",
        )
