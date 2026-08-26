from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.contracts.execution_result import (
    ExecutionResult,
)

from portable_ai.contracts.runtime_executor import (
    RuntimeExecutor,
)


class OllamaExecutor(RuntimeExecutor):
    """
    Execution adapter for Ollama runtime.
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
            model=request.model,
        )

        return ExecutionResult(
            runtime=request.runtime,
            model=request.model,
            response=response,
        )
