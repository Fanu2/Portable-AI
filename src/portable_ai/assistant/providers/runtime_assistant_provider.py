from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)

from portable_ai.contracts.runtime_provider import (
    RuntimeProvider,
)


class RuntimeAssistantProvider(
    AssistantProvider
):
    """
    Assistant provider adapter for runtime providers.

    Responsibilities:
        - adapt assistant context
        - delegate generation to runtime

    Does not:
        - manage runtimes
        - select models
        - manage provider lifecycle
    """

    def __init__(
        self,
        runtime_provider: RuntimeProvider,
    ) -> None:

        self._runtime_provider = (
            runtime_provider
        )

    def generate(
        self,
        context,
    ) -> str:
        """
        Generate assistant response.
        """

        prompt = str(
            context
        )

        return (
            self._runtime_provider
            .generate(
                prompt
            )
        )
