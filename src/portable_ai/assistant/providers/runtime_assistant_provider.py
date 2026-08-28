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
        - build runtime prompt
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

        if isinstance(
            context,
            str,
        ):
            prompt = context

        else:
            prompt = (
                self._build_prompt(
                    context
                )
            )

        return (
            self._runtime_provider
            .generate(
                prompt
            )
        )

    def _build_prompt(
        self,
        context,
    ) -> str:
        """
        Convert assistant prompt context
        into runtime prompt text.
        """

        parts = []

        if context.conversation:

            parts.append(
                "Conversation:\n"
                + str(
                    context.conversation
                )
            )

        if context.user_context:

            parts.append(
                "User Context:\n"
                + str(
                    context.user_context
                )
            )

        if context.retrieval_context:

            retrieved = "\n".join(
                result.content
                for result
                in context.retrieval_context
            )

            parts.append(
                "Retrieved Context:\n"
                + retrieved
            )

        if context.workspace_context:

            parts.append(
                "Workspace Context:\n"
                + str(
                    context.workspace_context
                )
            )

        if not parts:

            return ""

        return "\n\n".join(
            parts
        )
