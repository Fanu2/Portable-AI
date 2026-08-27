class ExecutionUIService:
    """
    GUI-facing execution boundary.

    Provides a simple interface for:
        - submitting prompts
        - receiving execution results

    Keeps GUI independent from
    execution internals.
    """

    def __init__(
        self,
        active_execution_service,
    ) -> None:

        self._execution = (
            active_execution_service
        )

    def execute(
        self,
        prompt: str,
    ):
        """
        Execute prompt using
        currently active model.
        """

        if not prompt:

            return None

        return self._execution.execute(
            prompt
        )
