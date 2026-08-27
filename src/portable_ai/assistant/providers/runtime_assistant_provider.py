from typing import Any

from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)


class RuntimeAssistantProvider(
    AssistantProvider
):
    """
    Adapter between assistant generation
    and runtime provider.

    Responsibilities:
        - translate assistant context
          into runtime prompt
        - delegate generation

    Does not:
        - manage runtime lifecycle
        - select models
        - manage UI
        - manage conversations

    Keeps assistant layer isolated
    from runtime implementations.
    """

    def __init__(
        self,
        runtime_provider,
    ) -> None:

        self._runtime = (
            runtime_provider
        )

    def generate(
        self,
        context: Any,
    ) -> str:
        """
        Generate assistant response.

        Context comes from:
            PromptContextService

        Runtime receives:
            prepared prompt string
        """

        prompt = (
            self._build_prompt(
                context
            )
        )

        return (
            self._runtime
            .generate(
                prompt
            )
        )

    def _build_prompt(
        self,
        context,
    ) -> str:
        """
        Convert assistant context
        into runtime prompt.

        Initial implementation:
            simple text boundary.

        Future:
            structured prompts,
            system instructions,
            workspace context.
        """

        if isinstance(
            context,
            str,
        ):

            return context

        return str(
            context
        )
