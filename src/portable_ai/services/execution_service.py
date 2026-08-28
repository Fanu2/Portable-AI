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
    Provides safe, validated model execution.

    Responsibilities:
        - locate the requested runtime executor
        - execute the prepared request
        - validate the execution result
        - return a valid ExecutionResult

    During development, diagnostic messages are
    printed when execution cannot complete.
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
        """
        Execute a prepared request using the
        requested runtime executor.
        """

        if request is None:

            print(
                "No execution request provided"
            )

            return None

        #
        # Locate the runtime executor.
        #
        executor = self._registry.get(
            executor_name
        )

        if executor is None:

            print(
                "No executor found:",
                executor_name,
            )

            return None

        #
        # Diagnostic request information.
        #
        print(
            "Execution request:",
            request,
        )

        #
        # Execute through the registered runtime.
        #
        try:

            result = executor.execute(
                request
            )

        except Exception as error:

            print(
                "Execution failed:",
                error,
            )

            return None

        #
        # Diagnostic execution result.
        #
        print(
            "Execution result:",
            result,
        )

        #
        # Validate the returned result.
        #
        if result is None:

            print(
                "Execution returned no result"
            )

            return None

        if not self._validator.validate(
            result
        ):

            print(
                "Execution result validation failed"
            )

            return None

        return result
