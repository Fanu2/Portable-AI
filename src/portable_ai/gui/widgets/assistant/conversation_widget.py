from PySide6.QtWidgets import (
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class ConversationWidget(QWidget):
    """
    Assistant conversation UI.

    Responsibilities:
        - display conversation
        - display conversation history
        - refresh UI from assistant state
        - accept user input
        - forward messages to UI service
        - render assistant responses
        - clear assistant session display

    Does not:
        - execute models
        - manage providers
        - access runtime layer

    AssistantService remains the source
    of truth for conversation state.
    """

    def __init__(
        self,
        assistant_ui_service,
    ) -> None:

        super().__init__()

        #
        # GUI-facing assistant boundary.
        #
        # UI communicates only through
        # AssistantUIService.
        #
        self._assistant = (
            assistant_ui_service
        )

        #
        # Conversation display.
        #
        self._display = QTextEdit()

        self._display.setReadOnly(
            True
        )

        #
        # User input.
        #
        self._input = QLineEdit()

        #
        # Actions.
        #
        self._send_button = QPushButton(
            "Send"
        )

        self._clear_button = QPushButton(
            "Clear"
        )

        #
        # Layout.
        #
        layout = QVBoxLayout()

        layout.addWidget(
            self._display
        )

        layout.addWidget(
            self._input
        )

        layout.addWidget(
            self._send_button
        )

        layout.addWidget(
            self._clear_button
        )

        self.setLayout(
            layout
        )

        #
        # Keep assistant area visible
        # inside ApplicationShellWidget.
        #
        self.setMinimumHeight(
            180
        )

        #
        # Events.
        #
        self._send_button.clicked.connect(
            self._send_message
        )

        self._clear_button.clicked.connect(
            self.clear_session
        )

    def load_history(
        self,
        messages,
    ) -> None:
        """
        Render conversation history.

        Expected message fields:
            - sender
            - content
        """

        self._display.clear()

        for message in messages:

            self._display.append(
                f"{message.sender}: {message.content}"
            )

    def refresh_history(
        self,
    ) -> None:
        """
        Refresh display from assistant state.

        Flow:

            AssistantService
                    |
                    ▼
            AssistantUIService
                    |
                    ▼
            ConversationWidget
                    |
                    ▼
              QTextEdit
        """

        history = (
            self._assistant
            .conversation_history()
        )

        self.load_history(
            history
        )

    def clear_session(
        self,
    ) -> None:
        """
        Clear assistant session.

        Delegates lifecycle control
        to AssistantUIService.

        UI does not manage:
            - conversation state
            - assistant context
            - persistence
        """

        self._assistant.clear()

        self._display.clear()

        self._input.clear()

    def _send_message(
        self,
    ) -> None:
        """
        Send user message.

        Flow:

            User input
                |
                ▼
            AssistantUIService
                |
                ▼
            AssistantService
                |
                ▼
            ResponseGenerationService
                |
                ▼
            Response
        """

        message = (
            self._input.text()
        )

        if not message:

            return

        #
        # Store user message.
        #
        self._assistant.send_message(
            message
        )

        #
        # Generate response.
        #
        response = (
            self._assistant
            .generate_response()
        )

        #
        # Refresh conversation
        # from service state.
        #
        self.refresh_history()

        #
        # Display generated response.
        #
        if response is not None:

            self._display.append(
                f"Assistant: {response}"
            )

        self._input.clear()
