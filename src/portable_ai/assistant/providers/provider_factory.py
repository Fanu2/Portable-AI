from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)


class ProviderFactory:
    """
    Creates assistant providers.

    Responsibilities:
        - construct provider instances
        - hide provider implementation details

    Does not:
        - execute models
        - select runtimes
        - manage conversations
    """

    def create(
        self,
        provider=None,
    ) -> AssistantProvider | None:
        """
        Return assistant provider.

        Current behavior:
            - accepts injected provider
            - returns None when no provider exists

        Future:
            - local provider selection
            - external provider selection
        """

        return provider
