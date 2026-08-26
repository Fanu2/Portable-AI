from portable_ai.contracts.execution_result import (
    ExecutionResult,
)


class ExecutionResultValidator:
    """
    Validates execution results.
    """

    def validate(
        self,
        result: ExecutionResult,
    ) -> bool:

        if not result.runtime:
            return False

        if not result.model:
            return False

        if not result.response:
            return False

        return True
