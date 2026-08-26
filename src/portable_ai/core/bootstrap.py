from portable_ai.contracts.application_context import (
    ApplicationContext,
)


class ApplicationBootstrap:
    """
    Builds the Portable-AI application context.
    """

    def __init__(
        self,
        context: ApplicationContext,
    ) -> None:
        self._context = context

    def build(self) -> ApplicationContext:
        return self._context
