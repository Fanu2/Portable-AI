from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from portable_ai.gui.widgets.runtime_details_widget import (
    RuntimeDetailsWidget,
)

from portable_ai.gui.widgets.runtime_selector_widget import (
    RuntimeSelectorWidget,
)


class DashboardWidget(QWidget):
    """
    Main dashboard display.
    """

    def __init__(
        self,
        dashboard_service,
    ) -> None:
        super().__init__()

        self._service = dashboard_service
        self._details = None

        self._title = QLabel(
            "Portable-AI Dashboard"
        )

        self._selector = RuntimeSelectorWidget(
            self._service.runtime_names()
        )

        self._selector.on_changed(
            self.refresh
        )

        self._runtime_label = QLabel()

        self._count_label = QLabel()

        self._refresh_button = QPushButton(
            "Refresh"
        )

        self._refresh_button.clicked.connect(
            self.refresh
        )

        self._layout = QVBoxLayout()

        self._layout.addWidget(
            self._title
        )

        self._layout.addWidget(
            self._selector
        )

        self._layout.addWidget(
            self._runtime_label
        )

        self._layout.addWidget(
            self._count_label
        )

        self._layout.addWidget(
            self._refresh_button
        )

        self.setLayout(
            self._layout
        )

        self.refresh()

    def refresh(self) -> None:
        summary = self._service.summary()

        runtimes = summary.get(
            "runtimes",
            {},
        )

        runtime_text = ""

        for name, status in runtimes.items():
            runtime_text += (
                f"\n{name.upper()}\n"
                "----------------\n"
                f"Status: "
                f"{'Online' if status else 'Offline'}\n"
            )

        self._runtime_label.setText(
            "Runtime Status\n"
            + runtime_text
        )

        self._count_label.setText(
            "Available Runtimes: "
            + str(
                summary.get(
                    "available_runtime_count",
                    0,
                )
            )
        )

        selected = self._selector.selected_runtime()

        snapshot = self._service.runtime_health_snapshot(
            selected
        )

        metadata = self._service.runtime_metadata(
            selected
        )

        details = {
            "health": snapshot.health.value,
            "checked_at": snapshot.checked_at,
            **metadata,
        }

        if self._details:
            self._details.refresh(
                details
            )
        else:
            self._details = RuntimeDetailsWidget(
                selected,
                details,
            )

            self._layout.addWidget(
                self._details
            )
