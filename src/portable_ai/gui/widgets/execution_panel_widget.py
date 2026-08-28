from PySide6.QtWidgets import (
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class ExecutionPanelWidget(QWidget):
    """
    User execution panel.

    Responsibilities:
        - collect prompt
        - submit execution request
        - display execution response

    Uses UI service boundary only.

    Does not:
        - manage runtimes
        - select models
        - execute directly
    """

    def __init__(
        self,
        execution_service,
    ) -> None:

        super().__init__()

        self._execution = (
            execution_service
        )

        #
        # Prompt input.
        #
        # QLineEdit is retained because
        # this is the existing UI contract.
        #
        self._prompt = QLineEdit()

        self._prompt.setPlaceholderText(
            "Enter prompt..."
        )

        #
        # Execute action.
        #
        self._execute_button = QPushButton(
            "Execute"
        )

        #
        # Execution response display.
        #
        # QTextEdit allows readable
        # multi-line AI responses.
        #
        self._result = QTextEdit()

        self._result.setReadOnly(
            True
        )

        self._result.setMinimumHeight(
            120
        )

        #
        # Layout.
        #
        layout = QVBoxLayout()

        layout.addWidget(
            self._prompt
        )

        layout.addWidget(
            self._execute_button
        )

        layout.addWidget(
            self._result
        )

        self.setLayout(
            layout
        )

        #
        # Events.
        #
        self._execute_button.clicked.connect(
            self.execute
        )

    def execute(
        self,
    ) -> None:
        """
        Execute current prompt.

        Uses execution UI boundary.
        """

        prompt = (
            self._prompt
            .text()
            .strip()
        )

        if not prompt:

            self._result.setPlainText(
                "Enter a prompt."
            )

            return

        result = (
            self._execution
            .execute(
                prompt
            )
        )

        if result is None:

            self._result.setPlainText(
                "No execution result."
            )

            return

        #
        # UI service returns the response
        # text boundary.
        #
        self._result.setPlainText(
            str(result)
        )
