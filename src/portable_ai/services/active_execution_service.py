class ActiveExecutionService:
    """
    Executes prompts using the currently
    active model.

    Responsibilities:
        - create execution request
        - forward request to execution adapter

    Does not select models.
    Does not manage runtimes.
    """

    def __init__(
        self,
        request_service,
        adapter_service,
    ) -> None:

        self._request_service = (
            request_service
        )

        self._adapter = (
            adapter_service
        )

    def execute(
        self,
        prompt: str,
    ):
        """
        Execute using active model.
        """

        request = (
            self._request_service
            .create_request(
                prompt
            )
        )

        if request is None:

            return None

        return self._adapter.execute(
            request
        )
