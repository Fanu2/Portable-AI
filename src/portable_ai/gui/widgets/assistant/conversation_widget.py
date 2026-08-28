from PySide6.QtGui import QKeySequence, QShortcut
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
        - show generation state
        - handle UI errors
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

        self._assistant = (
            assistant_ui_service
        )

        self._generating = False

        #
        # Conversation display.
        #
        # Read-only assistant conversation view.
        #
        self._display = QTextEdit()

        self._display.setReadOnly(
            True
        )

        #
        # Preserve visible conversation area
        # when composed with dashboard
        # and execution panels.
        #
        self._display.setMinimumHeight(
            180
        )
        #
        # Input.
        #
        self._input = QLineEdit()

        self._input.setPlaceholderText(
            "Enter message..."
        )

        #
        # Actions.
        #
        self._send_button = QPushButton(
            "Send"
        )

        self._clear_button = QPushButton(
            "Clear"
        )

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

        self.setMinimumHeight(
            300
        )

        #
        # Events.
        #
        self._send_button.clicked.connect(
            self._send_message
        )

        self._input.returnPressed.connect(
            self._send_message
        )

        self._clear_button.clicked.connect(
            self.clear_session
        )

        #
        # Future multiline support.
        #
        shortcut = QShortcut(
            QKeySequence(
                "Ctrl+Return"
            ),
            self,
        )

        shortcut.activated.connect(
            self._send_message
        )

    def _scroll_to_bottom(
        self,
    ) -> None:
        """
        Keep latest message visible.
        """

        scrollbar = (
            self._display
            .verticalScrollBar()
        )

        scrollbar.setValue(
            scrollbar.maximum()
        )

    def _format_message(
        self,
        sender: str,
        content: str,
    ) -> str:
        """
        Preserve text contract.

        Existing tests depend on:

            User: message
            Assistant: response
        """

        return (
            f"{sender}: {content}"
        )

    def _append_message(
        self,
        sender: str,
        content: str,
    ) -> None:
        """
        Append message to display.
        """

        print(
            "DISPLAY APPEND:",
            sender,
            content,
        )

        self._display.append(
            self._format_message(
                sender,
                content,
            )
        )

        self._scroll_to_bottom()

    def append_assistant_chunk(
        self,
        chunk: str,
    ) -> None:
        """
        Future streaming hook.

        Reserved for incremental
        assistant responses.

        Currently UI only.
        """

        self._display.insertPlainText(
            chunk
        )

        self._scroll_to_bottom()

    def _show_status(
        self,
        text: str,
    ) -> None:
        """
        Display temporary assistant state.
        """

        self._append_message(
            "Assistant",
            text,
        )

    def _set_generating(
        self,
        active: bool,
    ) -> None:
        """
        Lock UI during generation.
        """

        self._generating = active

        self._send_button.setEnabled(
            not active
        )

        self._input.setEnabled(
            not active
        )

    def load_history(
        self,
        messages,
    ) -> None:
        """
        Render conversation history.
        """

        self._display.clear()

        for message in messages:

            sender = (
                message.sender
                .capitalize()
            )

            self._append_message(
                sender,
                message.content,
            )

        self._scroll_to_bottom()

    def refresh_history(
        self,
    ) -> None:
        """
        Refresh display from assistant state.
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
        """

        self._assistant.clear()

        self._display.clear()

        self._input.clear()

    def _send_message(
        self,
    ) -> None:
        """
        Send user message and generate response.
        """

        if self._generating:

            return

        message = (
            self._input.text()
            .strip()
        )

        if not message:

            return

        self._input.clear()

        try:

            self._set_generating(
                True
            )

            self._assistant.send_message(
                message
            )

            self.refresh_history()

            self._show_status(
                "Thinking..."
            )

            response = (
                self._assistant
                .generate_response()
            )

            if response:

                self.refresh_history()

            else:

                self._append_message(
                    "Assistant",
                    "No response.",
                )

        except Exception as error:

            self._append_message(
                "Assistant",
                f"Error: {error}",
            )

        finally:

            self._set_generating(
                False
            )
