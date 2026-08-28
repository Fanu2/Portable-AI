from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)


class ExecutionAdapterService:
    """
    Adapter between execution requests
    and the execution engine.

    Responsibilities:
        - validate request presence
        - extract the requested runtime
        - forward execution to ExecutionService

    Does not:
        - execute models directly
        - manage active model state
        - select models
        - manage runtimes
    """

    def __init__(
        self,
        execution_service,
    ) -> None:

        self._execution = (
            execution_service
        )

    def execute(
        self,
        request: ExecutionRequest,
    ):
        """
        Execute a prepared request.

        The ExecutionRequest contains the
        runtime name required by
        ExecutionService to locate the
        appropriate executor.
        """

        if request is None:

            return None

        return self._execution.execute(
            request.runtime,
            request,
        )
