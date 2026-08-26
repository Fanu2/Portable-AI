from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class RuntimeControlWidget(QWidget):
    """
    Displays runtime control information.
    """

    def __init__(
        self,
        dashboard_service,
    ) -> None:

        super().__init__()

        self._service = dashboard_service

        self._label = QLabel()

        self._refresh_button = QPushButton(
            "Refresh Health"
        )

        self._refresh_button.clicked.connect(
            self.refresh
        )

        layout = QVBoxLayout()

        layout.addWidget(
            self._label
        )

        layout.addWidget(
            self._refresh_button
        )

        self.setLayout(
            layout
        )

        self.refresh()

    def refresh(
        self,
    ) -> None:

        runtimes = (
            self._service.runtime_names()
        )

        text = (
            "Runtime Control\n"
            "----------------\n"
        )

        for runtime in runtimes:

            snapshot = (
                self._service.runtime_health_snapshot(
                    runtime
                )
            )

            metadata = (
                self._service.runtime_metadata(
                    runtime
                )
            )

            text += (
                f"{runtime.upper()}\n"
                f"Status: "
                f"{snapshot.health.value}\n"
                f"Endpoint: "
                f"{metadata.get('endpoint', '')}\n"
                f"Capabilities: "
                f"{', '.join(metadata.get('capabilities', []))}\n\n"
            )

        self._label.setText(
            text
        )
