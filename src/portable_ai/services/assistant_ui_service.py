class AssistantUIService:
    """
    GUI-facing assistant boundary.

    Responsibilities:
        - receive UI messages
        - expose assistant state to UI
        - request assistant responses
        - provide conversation history
        - provide workspace context
        - clear assistant session
        - forward requests to AssistantService

    Does not:
        - execute models
        - manage runtimes
        - select providers
        - call tools directly
        - manage workspace data

    The UI communicates only through
    this boundary.

    State ownership remains inside
    AssistantService.
    """

    def __init__(
        self,
        assistant_service,
    ) -> None:

        #
        # Assistant coordination layer.
        #
        # Contains:
        #   - conversation handling
        #   - assistant context
        #   - prompt preparation
        #   - response generation boundary
        #   - session lifecycle
        #   - workspace context boundary
        #
        self._assistant = (
            assistant_service
        )

    def send_message(
        self,
        message: str,
    ):
        """
        Send user message.

        Delegates storage to
        AssistantService.

        Returns updated conversation
        state for UI refresh.
        """

        if not message:

            return None

        #
        # AssistantService owns
        # conversation state.
        #
        self._assistant.send_message(
            message
        )

        #
        # Return current state.
        #
        return (
            self._assistant
            .conversation_history()
        )

    def conversation_history(
        self,
    ):
        """
        Return current conversation state.

        UI uses this method to refresh
        displayed messages.

        UI does not maintain its own
        conversation state.
        """

        return (
            self._assistant
            .conversation_history()
        )

    def generate_response(
        self,
    ):
        """
        Request assistant response.

        Delegates response generation
        through AssistantService.

        UI does not know about:
            - executors
            - runtimes
            - providers
            - models
        """

        return (
            self._assistant
            .generate_response()
        )

    def prompt_context(
        self,
    ):
        """
        Return prepared assistant
        prompt context.

        UI can inspect context
        without accessing assistant
        internals.
        """

        return (
            self._assistant
            .prompt_context()
        )

    def workspace_context(
        self,
    ):
        """
        Return workspace context.

        Provides UI visibility into
        workspace state.

        UI does not manage:
            - documents
            - indexing
            - retrieval
            - storage
        """

        return (
            self._assistant
            .workspace_context()
        )

    def clear(
        self,
    ) -> None:
        """
        Clear assistant session.

        Delegates lifecycle control
        to AssistantService.

        UI does not directly manage:
            - conversation state
            - assistant context
            - workspace state
            - persistence
        """

        self._assistant.clear()
