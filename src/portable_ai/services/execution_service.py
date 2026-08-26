from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.contracts.execution_result import (
    ExecutionResult,
)

from portable_ai.models.executor_registry import (
    ExecutorRegistry,
)

from portable_ai.services.execution_result_validator import (
    ExecutionResultValidator,
)


class ExecutionService:
    """
    Provides safe validated execution.
    """

    def __init__(
        self,
        registry: ExecutorRegistry,
        validator: ExecutionResultValidator,
    ) -> None:
        self._registry = registry
        self._validator = validator

    def execute(
        self,
        executor_name: str,
        request: ExecutionRequest,
    ) -> ExecutionResult | None:

        executor = self._registry.get(
            executor_name
        )

        if executor is None:
            return None

        try:
            result = executor.execute(
                request
            )

        except Exception:
            return None

        if not self._validator.validate(
            result
        ):
            return None

        return result
