from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)


class ExecutionAssistantProvider(
    AssistantProvider
):
    """
    Assistant provider using the active
    execution pipeline.

    Responsibilities:
        - prepare assistant prompt
        - delegate execution
        - return response text

    Does not:
        - select models
        - select runtimes
        - execute directly
        - manage conversation state
    """

    def __init__(
        self,
        active_execution_service,
    ) -> None:

        self._execution = (
            active_execution_service
        )

    def generate(
        self,
        context,
    ) -> str:

        prompt = (
            self._build_prompt(
                context
            )
        )

        if not prompt:

            return ""

        try:

            result = (
                self._execution
                .execute(
                    prompt
                )
            )

        except Exception as error:

            print(
                "Assistant execution failed:",
                error,
            )

            return ""

        if result is None:

            return ""

        return (
            result.response
            or ""
        )

    def _build_prompt(
        self,
        context,
    ) -> str:

        parts = [
            "You are a helpful local AI assistant.",
            "Answer the user clearly and concisely.",
        ]

        if context.conversation:

            parts.append(
                "Conversation:\n"
                + self._format(
                    context.conversation
                )
            )

        if context.user_context:

            parts.append(
                "User Context:\n"
                + self._format(
                    context.user_context
                )
            )

        if context.retrieval_context:

            parts.append(
                "Retrieved Context:\n"
                + self._format(
                    context.retrieval_context
                )
            )

        if context.workspace_context:

            parts.append(
                "Workspace Context:\n"
                + self._format(
                    context.workspace_context
                )
            )

        return "\n\n".join(
            parts
        )

    def _format(
        self,
        value,
    ) -> str:

        if isinstance(
            value,
            list,
        ):

            return "\n".join(
                str(item)
                for item in value
            )

        if isinstance(
            value,
            dict,
        ):

            return "\n".join(
                f"{key}: {item}"
                for key, item
                in value.items()
            )

        return str(
            value
        )
