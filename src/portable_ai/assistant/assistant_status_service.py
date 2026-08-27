class AssistantStatusService:
    """
    Reports assistant capability status.

    Responsibilities:
        - report provider availability
        - report runtime readiness
        - expose generation capability state

    Does not:
        - execute generation
        - manage runtimes
        - load models
        - manage UI
    """

    def __init__(
        self,
        provider=None,
    ) -> None:

        self._provider = provider

    def available(
        self,
    ) -> bool:
        """
        Return whether assistant
        generation is configured.
        """

        return (
            self._provider
            is not None
        )

    def health(
        self,
    ) -> dict:
        """
        Return assistant status.

        Safe reporting boundary.
        """

        if self._provider is None:

            return {
                "available": False,
                "provider": None,
                "runtime": False,
            }

        runtime_health = True

        if hasattr(
            self._provider,
            "health",
        ):

            runtime_health = (
                self._provider.health()
            )

        return {
            "available": True,
            "provider": (
                self._provider.__class__
                .__name__
            ),
            "runtime": runtime_health,
        }
