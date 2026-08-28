from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class ConversationWidget(QWidget):
    """
    Controlled assistant conversation UI.

    Responsibilities:
        - collect user messages
        - send messages to assistant
        - request assistant responses
        - display conversation output

    Uses AssistantUIService only.
    """

    def __init__(
        self,
        assistant_service,
    ) -> None:

        super().__init__()

        self._assistant = (
            assistant_service
        )

        self._history = QLabel()

        self._history.setWordWrap(
            True
        )

        self._input = QTextEdit()

        self._input.setPlaceholderText(
            "Enter message..."
        )

        self._send_button = QPushButton(
            "Send"
        )

        self._send_button.clicked.connect(
            self.send
        )

        layout = QVBoxLayout()

        layout.addWidget(
            self._history
        )

        layout.addWidget(
            self._input
        )

        layout.addWidget(
            self._send_button
        )

        self.setLayout(
            layout
        )

    def send(
        self,
    ) -> None:
        """
        Send user message and request
        assistant response.
        """

        message = (
            self._input
            .toPlainText()
            .strip()
        )

        if not message:

            return

        self._assistant.send_message(
            message
        )

        response = (
            self._assistant
            .generate_response()
        )

        if response is None:

            response = (
                "No assistant response."
            )

        self._history.setText(
            f"User:\n{message}\n\n"
            f"Assistant:\n{response}"
        )

        self._input.clear()
