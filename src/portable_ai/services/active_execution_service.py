class ActiveExecutionService:
    """
    Executes prompts using the currently
    active model.

    Responsibilities:
        - create execution request
        - verify runtime readiness
        - forward request to execution adapter

    Does not select models.
    Does not manage runtimes.
    """

    def __init__(
        self,
        request_service,
        adapter_service,
        readiness_service=None,
    ) -> None:

        self._request_service = (
            request_service
        )

        self._adapter = (
            adapter_service
        )

        self._readiness = (
            readiness_service
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

        if self._readiness is not None:

            readiness = (
                self._readiness.check(
                    request.runtime
                )
            )

            if not readiness.ready:

                return None

        return self._adapter.execute(
            request
        )
