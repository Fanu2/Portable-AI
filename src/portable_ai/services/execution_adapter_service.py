from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)


class ExecutionAdapterService:
    """
    Adapter between execution requests
    and the execution engine.

    Responsibilities:
        - validate request presence
        - forward request to ExecutionService

    Does not execute models directly.
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
        """

        if request is None:

            return None

        return self._execution.execute(
            request
        )
