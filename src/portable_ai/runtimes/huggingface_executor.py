from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.contracts.execution_result import (
    ExecutionResult,
)

from portable_ai.contracts.runtime_executor import (
    RuntimeExecutor,
)


class HuggingFaceExecutor(RuntimeExecutor):
    """
    Execution adapter for the local
    Hugging Face runtime.
    """

    def __init__(
        self,
        provider,
    ) -> None:

        self._provider = provider

    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:

        response = self._provider.generate(
            request.prompt,
        )

        return ExecutionResult(
            runtime=request.runtime,
            model=request.model,
            response=response,
        )
