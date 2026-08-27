from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)


class ResponseGenerationService:
    """
    Assistant response generation boundary.

    Responsibilities:
        - receive prepared prompt context
        - delegate generation to provider

    Does not:
        - manage models
        - select runtimes
        - execute infrastructure
        - know provider details

    Provider implementations are injected
    through AssistantProvider contract.
    """

    def __init__(
        self,
        provider: AssistantProvider | None = None,
    ) -> None:

        self._provider = provider

    def generate(
        self,
        prompt_context,
    ):
        """
        Generate assistant response.

        Returns None when no provider
        is configured.
        """

        if self._provider is None:

            return None

        return (
            self._provider
            .generate(
                prompt_context
            )
        )
