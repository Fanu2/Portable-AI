from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
)

from portable_ai.gui.widgets.application_shell_widget import (
    ApplicationShellWidget,
)

from portable_ai.gui.widgets.dashboard_widget import (
    DashboardWidget,
)


class MainWindow(QMainWindow):
    """
    Main Portable-AI application window.

    Responsibilities:
        - create application window
        - assemble GUI components
        - connect UI context

    Architecture:

        ApplicationContext
              |
              v
        DashboardWidget


        UIContext
              |
        ┌─────┴──────────────┐
        v                    v

    ExecutionUI        AssistantUI
                           |
                           v
                  WorkspaceStatusUI


        All composed by:
              |
              v
        ApplicationShellWidget

    Core services remain isolated.
    """

    def __init__(
        self,
        context=None,
        ui_context=None,
        title: str = "Portable-AI",
    ) -> None:

        super().__init__()

        #
        # Core application services.
        #
        self._context = context

        #
        # GUI service boundary.
        #
        self._ui_context = ui_context

        self.setWindowTitle(
            title
        )

        self.resize(
            1000,
            700,
        )

        self._dashboard_widget = None

        self._shell_widget = None

        self._setup_dashboard()

    def _setup_dashboard(
        self,
    ) -> None:
        """
        Build complete application UI.
        """

        if self._context is None:

            self.setCentralWidget(
                QLabel(
                    "Portable-AI"
                )
            )

            return

        #
        # Create dashboard widget.
        #
        if hasattr(
            self._context,
            "dashboard",
        ):

            self._dashboard_widget = (
                DashboardWidget(
                    dashboard_service=(
                        self._context.dashboard
                    ),

                    hardware_service=getattr(
                        self._context,
                        "hardware_detection",
                        None,
                    ),

                    model_inventory_service=getattr(
                        self._context,
                        "model_inventory",
                        None,
                    ),

                    model_compatibility_service=getattr(
                        self._context,
                        "model_compatibility",
                        None,
                    ),

                    runtime_control_service=getattr(
                        self._context,
                        "runtime_control",
                        None,
                    ),
                )
            )

        else:

            self._dashboard_widget = (
                DashboardWidget(
                    self._context
                )
            )

        #
        # Extract GUI service boundaries.
        #
        execution_service = None

        assistant_service = None

        if self._ui_context is not None:

            if (
                self._ui_context.execution
                is not None
            ):

                execution_service = (
                    self._ui_context.execution
                )

            if (
                self._ui_context.assistant
                is not None
            ):

                assistant_service = (
                    self._ui_context.assistant
                )

        #
        # Compose application shell.
        #
        # Shell owns:
        #   - DashboardWidget
        #   - ExecutionPanelWidget
        #   - AssistantPanelWidget
        #   - WorkspaceStatusWidget
        #
        self._shell_widget = (
            ApplicationShellWidget(
                self._dashboard_widget,
                execution_service,
                assistant_service,
            )
        )

        self.setCentralWidget(
            self._shell_widget
        )
