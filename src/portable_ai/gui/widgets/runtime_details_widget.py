from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class RuntimeDetailsWidget(QWidget):
    """
    Displays runtime details.
    """

    def __init__(
        self,
        name: str,
        details: dict,
    ) -> None:
        super().__init__()

        self._name = name
        self._details = details

        self._label = QLabel()

        layout = QVBoxLayout()

        layout.addWidget(
            self._label
        )

        self.setLayout(
            layout
        )

        self.refresh(
            details
        )

    def refresh(
        self,
        details: dict,
    ) -> None:
        self._details = details

        health = details.get(
            "health",
            "unknown",
        )

        checked_at = details.get(
            "checked_at",
            "unknown",
        )

        endpoint = details.get(
            "endpoint",
            "unknown",
        )

        capabilities = details.get(
            "capabilities",
            [],
        )

        self._label.setText(
            f"{self._name.upper()}\n"
            "----------------\n"
            f"Health: {health.upper()}\n"
            f"Checked: {checked_at}\n"
            f"Endpoint: {endpoint}\n"
            f"Capabilities: "
            f"{', '.join(capabilities)}"
        )
