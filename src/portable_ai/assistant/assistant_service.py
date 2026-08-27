from portable_ai.assistant.conversation_service import (
    ConversationService,
)

from portable_ai.assistant.context_service import (
    AssistantContextService,
)

from portable_ai.assistant.prompt_context_service import (
    PromptContextService,
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

    Does not:
        - manage models
        - select runtimes
        - directly execute runtimes
        - call tools
        - run autonomous tasks
        - manage workspace data

    This service composes assistant
    foundation components only.

    Session state remains in-memory.
    Persistence is intentionally
    outside this boundary.
    """

    def __init__(
        self,
        conversation_service: ConversationService | None = None,
        context_service: AssistantContextService | None = None,
        prompt_context_service: PromptContextService | None = None,
        response_generation_service: ResponseGenerationService | None = None,
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

        #
        # In-memory assistant session.
        #
        # Owns:
        #   - conversation state
        #   - assistant context
        #   - workspace boundary
        #
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

    def generate_response(
        self,
    ):
        """
        Generate assistant response.

        Uses only the response
        generation boundary.

        Does not directly access:
            - models
            - runtimes
            - executors
        """

        return (
            self._response_generation
            .generate(
                self._prompt_context
                .get_context()
            )
        )

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

        Future assistant engines consume
        this boundary.
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

        Synchronizes:
            - conversation
            - assistant context
            - workspace context

        Workspace remains a boundary only.

        Persistence is intentionally
        not implemented here.
        """

        self._session.conversation = (
            self._conversation.history()
        )

        self._session.context = (
            self._context.get_context()
        )

        #
        # Make workspace context available
        # to future prompt construction.
        #
        self._prompt_context.set_workspace_context(
            self._session.workspace
        )

        return self._session

    def workspace_context(
        self,
    ) -> WorkspaceContext:
        """
        Return current workspace context.

        Assistant can see workspace state.

        Assistant does not manage:
            - documents
            - indexing
            - retrieval
            - storage
        """

        return (
            self._session.workspace
        )

    def clear(
        self,
    ) -> None:
        """
        Reset assistant state.

        Clears:
            - conversation history
            - prompt conversation context
            - session state
        """

        self._conversation.clear()

        self._prompt_context.set_conversation(
            []
        )

        self._session = (
            AssistantSession()
        )

        #
        # Reset workspace-aware prompt state.
        #
        self._prompt_context.set_workspace_context(
            self._session.workspace
        )
