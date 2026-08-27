from portable_ai.contracts.assistant_context import (
    AssistantContext,
)


class AssistantContextService:
    """
    Manages assistant session context.

    Responsibilities:
        - create assistant context
        - update context values
        - retrieve current context

    Does not:
        - execute models
        - manage runtimes
        - call tools
        - perform autonomous actions

    Keeps assistant state isolated from:
        - ApplicationContext
        - UIContext
        - Execution services
    """

    def __init__(
        self,
        context: AssistantContext | None = None,
    ) -> None:

        # Store current assistant context.
        #
        # A default empty context allows
        # the service to be created before
        # a conversation starts.
        self._context = (
            context
            or AssistantContext()
        )

    def get_context(
        self,
    ) -> AssistantContext:
        """
        Return current assistant context.
        """

        return self._context

    def update_context(
        self,
        context: AssistantContext,
    ) -> None:
        """
        Replace current assistant context.

        Context is immutable, so replacement
        is used instead of mutation.
        """

        self._context = context

    def set_user_context(
        self,
        user_context: dict,
    ) -> None:
        """
        Update user-related assistant context.
        """

        self._context = AssistantContext(
            conversation_id=(
                self._context.conversation_id
            ),
            user_context=user_context,
        )

    def set_conversation_id(
        self,
        conversation_id: str,
    ) -> None:
        """
        Set active conversation identifier.
        """

        self._context = AssistantContext(
            conversation_id=conversation_id,
            user_context=(
                self._context.user_context
            ),
        )
