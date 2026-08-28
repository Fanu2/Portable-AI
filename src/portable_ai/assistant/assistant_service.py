from portable_ai.assistant.conversation_service import (
    ConversationService,
)

from portable_ai.assistant.context_service import (
    AssistantContextService,
)

from portable_ai.assistant.prompt_context_service import (
    PromptContextService,
)

from portable_ai.assistant.retrieval_context_service import (
    RetrievalContextService,
)

from portable_ai.assistant.response_generation_service import (
    ResponseGenerationService,
)

from portable_ai.assistant.session.session_contract import (
    AssistantSession,
)

from portable_ai.workspace.workspace_context import (
    WorkspaceContext,
)


class AssistantService:
    """
    Main assistant coordination boundary.

    Responsibilities:
        - coordinate conversation state
        - coordinate assistant context
        - maintain assistant session state
        - expose workspace context boundary
        - prepare prompt context
        - request response generation
        - expose retrieval context bridge

    Does not:
        - manage models
        - select runtimes
        - directly execute runtimes
        - call tools
        - run autonomous tasks
        - manage workspace data
        - perform retrieval directly

    Session state remains in-memory.
    Persistence is outside this boundary.
    """

    def __init__(
        self,
        conversation_service: ConversationService | None = None,
        context_service: AssistantContextService | None = None,
        prompt_context_service: PromptContextService | None = None,
        response_generation_service: ResponseGenerationService | None = None,
        retrieval_context_service: RetrievalContextService | None = None,
    ) -> None:

        self._conversation = (
            conversation_service
            or ConversationService()
        )

        self._context = (
            context_service
            or AssistantContextService()
        )

        self._prompt_context = (
            prompt_context_service
            or PromptContextService()
        )

        self._response_generation = (
            response_generation_service
            or ResponseGenerationService()
        )

        self._retrieval_context = (
            retrieval_context_service
        )

        self._session = (
            AssistantSession()
        )

    def send_message(
        self,
        message: str,
    ) -> None:
        """
        Store user message.

        Updates:
            - conversation state
            - prompt context
            - session state
            - retrieval context when configured
        """

        self._conversation.add_message(
            "user",
            message,
        )

        self._prompt_context.set_conversation(
            self._conversation.history()
        )

        self._session.conversation = (
            self._conversation.history()
        )

        if self._retrieval_context is not None:

            self.retrieve_context(
                message
            )

    def retrieve_context(
        self,
        query: str,
    ) -> None:
        """
        Update prompt context with retrieval results.

        Retrieval remains outside assistant core.
        """

        if self._retrieval_context is None:
            return

        self._retrieval_context.update(
            query
        )

    def generate_response(
        self,
    ):
        """
        Generate assistant response.

        Generated responses become part
        of assistant conversation state.
        """

        response = (
            self._response_generation
            .generate(
                self._prompt_context
                .get_context()
            )
        )

        if response:

            self._conversation.add_message(
                "assistant",
                response,
            )

            self._prompt_context.set_conversation(
                self._conversation.history()
            )

            self._session.conversation = (
                self._conversation.history()
            )

        return response

    def conversation_history(
        self,
    ):
        """
        Return conversation history.
        """

        return (
            self._conversation.history()
        )

    def context(
        self,
    ):
        """
        Return assistant context.
        """

        return (
            self._context.get_context()
        )

    def prompt_context(
        self,
    ):
        """
        Return prepared prompt context.
        """

        return (
            self._prompt_context
            .get_context()
        )

    def session(
        self,
    ) -> AssistantSession:
        """
        Return current assistant session.
        """

        self._session.conversation = (
            self._conversation.history()
        )

        self._session.context = (
            self._context.get_context()
        )

        self._prompt_context.set_workspace_context(
            self._session.workspace
        )

        return self._session

    def workspace_context(
        self,
    ) -> WorkspaceContext:
        """
        Return current workspace context.
        """

        return (
            self._session.workspace
        )

    def clear(
        self,
    ) -> None:
        """
        Reset assistant state.
        """

        self._conversation.clear()

        self._prompt_context.set_conversation(
            []
        )

        self._session = (
            AssistantSession()
        )

        self._prompt_context.set_workspace_context(
            self._session.workspace
        )
