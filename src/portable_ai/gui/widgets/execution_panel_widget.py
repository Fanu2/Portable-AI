from PySide6.QtWidgets import (
    QLabel,
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
        - display result

    Uses UI service boundary only.
    """

    def __init__(
        self,
        execution_service,
    ) -> None:

        super().__init__()

        self._execution = (
            execution_service
        )

        self._prompt = QTextEdit()

        self._prompt.setPlaceholderText(
            "Enter prompt..."
        )

        self._execute_button = QPushButton(
            "Execute"
        )

        self._result = QLabel()

        self._execute_button.clicked.connect(
            self.execute
        )

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

    def execute(
        self,
    ) -> None:

        prompt = (
            self._prompt
            .toPlainText()
            .strip()
        )

        result = (
            self._execution.execute(
                prompt
            )
        )

        if result is None:

            self._result.setText(
                "No execution result"
            )

            return

        self._result.setText(
            str(result)
        )
