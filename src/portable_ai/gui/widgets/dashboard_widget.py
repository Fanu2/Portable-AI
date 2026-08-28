from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from portable_ai.gui.widgets.active_model_widget import (
    ActiveModelWidget,
)

from portable_ai.gui.widgets.hardware_widget import (
    HardwareWidget,
)

from portable_ai.gui.widgets.model_inventory_widget import (
    ModelInventoryWidget,
)

from portable_ai.gui.widgets.model_management_widget import (
    ModelManagementWidget,
)

from portable_ai.gui.widgets.model_selection_widget import (
    ModelSelectionWidget,
)

from portable_ai.gui.widgets.runtime_control_widget import (
    RuntimeControlWidget,
)

from portable_ai.gui.widgets.runtime_details_widget import (
    RuntimeDetailsWidget,
)

from portable_ai.gui.widgets.runtime_selector_widget import (
    RuntimeSelectorWidget,
)


class DashboardWidget(QWidget):
    """
    Main Portable-AI dashboard.

    UI responsibility:
        - Display system intelligence
        - Display model intelligence
        - Display runtime state

    Service responsibility:
        - Model selection
        - Compatibility decisions
        - Runtime operations

    This widget remains a presentation layer only.
    """

    def __init__(
        self,
        dashboard_service,
        hardware_service=None,
        model_inventory_service=None,
        model_compatibility_service=None,
        model_selection_service=None,
        active_model_service=None,
        runtime_control_service=None,
    ) -> None:

        super().__init__()

        self._service = dashboard_service

        # Child widgets
        self._hardware = None
        self._models = None
        self._model_management = None
        self._model_selection = None
        self._active_model = None
        self._runtime_control = None
        self._details = None

        # Dashboard title
        self._title = QLabel(
            "Portable-AI Dashboard"
        )

        # Runtime selector
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

        # -------------------------------------------------
        # Hardware intelligence
        #
        # Shows:
        #   CPU
        #   RAM
        #   Storage
        # -------------------------------------------------

        if hardware_service is not None:

            self._hardware = HardwareWidget(
                hardware_service
            )

            self._layout.addWidget(
                self._hardware
            )

        # -------------------------------------------------
        # Model intelligence
        #
        # Inventory:
        #   Available models
        #
        # Management:
        #   Compatibility status
        #
        # Selection:
        #   User-selected active model
        #
        # Active:
        #   Current model state
        # -------------------------------------------------

        if model_inventory_service is not None:

            self._models = ModelInventoryWidget(
                model_inventory_service
            )

            self._layout.addWidget(
                self._models
            )

            self._model_management = (
                ModelManagementWidget(
                    model_inventory_service,
                    model_compatibility_service,
                    hardware_service,
                )
            )

            self._layout.addWidget(
                self._model_management
            )

        if (
            model_inventory_service is not None
            and active_model_service is not None
        ):

            #
            # Model selection.
            #
            # The activation callback refreshes the
            # dashboard immediately after the active
            # model state changes.
            #
            self._model_selection = (
                ModelSelectionWidget(
                    model_inventory_service,
                    active_model_service,
                    on_activated=self.refresh,
                )
            )

            self._layout.addWidget(
                self._model_selection
            )

        if active_model_service is not None:

            self._active_model = (
                ActiveModelWidget(
                    active_model_service
                )
            )

            self._layout.addWidget(
                self._active_model
            )

        # -------------------------------------------------
        # Runtime control
        # -------------------------------------------------

        if runtime_control_service is not None:

            self._runtime_control = (
                RuntimeControlWidget(
                    runtime_control_service
                )
            )

            self._layout.addWidget(
                self._runtime_control
            )

        # -------------------------------------------------
        # Runtime overview
        # -------------------------------------------------

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

    def refresh(
        self,
    ) -> None:

        # -------------------------------------------------
        # Runtime summary
        # -------------------------------------------------

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

        # -------------------------------------------------
        # Runtime detail panel
        # -------------------------------------------------

        selected = (
            self._selector.selected_runtime()
        )

        snapshot = (
            self._service.runtime_health_snapshot(
                selected
            )
        )

        metadata = (
            self._service.runtime_metadata(
                selected
            )
        )

        details = {
            "health": snapshot.health.value,
            "checked_at": snapshot.checked_at,
            **metadata,
        }

        if self._details is None:

            self._details = RuntimeDetailsWidget(
                selected,
                details,
            )

            self._layout.addWidget(
                self._details
            )

        else:

            self._details.refresh(
                details
            )

        # -------------------------------------------------
        # Refresh child widgets
        # -------------------------------------------------

        if self._hardware is not None:

            self._hardware.refresh()

        if self._models is not None:

            self._models.refresh()

        if self._model_management is not None:

            self._model_management.refresh()

        if self._model_selection is not None:

            self._model_selection.refresh()

        if self._active_model is not None:

            self._active_model.refresh()

        if self._runtime_control is not None:

            self._runtime_control.refresh()
