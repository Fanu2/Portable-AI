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
        - create the application window
        - compose top-level GUI components
        - connect core and GUI contexts
        - keep presentation composition separate
          from application logic

    Architecture:

        ApplicationContext
              |
              +----------------------------+
              |                            |
              v                            v
        DashboardWidget              UI service boundaries
              |                            |
              |                    +-------+-------+
              |                    |               |
              |                    v               v
              |              Execution UI    Assistant UI
              |                                      |
              |                                      v
              |                              Workspace Status
              |
              +-------------+
                            |
                            v
                ApplicationShellWidget

    Core services remain owned by
    ApplicationFactory and ApplicationContext.

    GUI service boundaries remain owned by
    UIFactory and UIContext.

    MainWindow performs composition only.
    """

    def __init__(
        self,
        context=None,
        ui_context=None,
        title: str = "Portable-AI",
    ) -> None:

        super().__init__()

        #
        # Core application context.
        #
        self._context = context

        #
        # GUI-facing service context.
        #
        self._ui_context = ui_context

        #
        # Window configuration.
        #
        self.setWindowTitle(
            title
        )

        self.resize(
            1000,
            700,
        )

        #
        # Top-level widgets.
        #
        self._dashboard_widget = None

        self._shell_widget = None

        #
        # Build application UI.
        #
        self._setup_dashboard()

    def _setup_dashboard(
        self,
    ) -> None:
        """
        Build the complete application UI.

        The dashboard receives core services.

        Execution and assistant panels receive
        GUI-facing service boundaries.

        ApplicationShellWidget owns the final
        visual composition.
        """

        #
        # Fallback when no application context
        # has been supplied.
        #
        if self._context is None:

            self.setCentralWidget(
                QLabel(
                    "Portable-AI"
                )
            )

            return

        #
        # Create dashboard.
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

                    model_query_service=getattr(
                        self._context,
                        "model_query",
                        None,
                    ),

                    model_compatibility_service=getattr(
                        self._context,
                        "model_compatibility",
                        None,
                    ),

                    #
                    # Model selection capability.
                    #
                    # Enables model selection when
                    # the required services are
                    # available.
                    #
                    model_selection_service=getattr(
                        self._context,
                        "model_selection",
                        None,
                    ),

                    #
                    # Active model state.
                    #
                    # Used by:
                    #   - ModelSelectionWidget
                    #   - ActiveModelWidget
                    #
                    active_model_service=getattr(
                        self._context,
                        "active_model",
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

            #
            # Backward-compatible dashboard path.
            #
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

            execution_service = getattr(
                self._ui_context,
                "execution",
                None,
            )

            assistant_service = getattr(
                self._ui_context,
                "assistant",
                None,
            )

        #
        # Compose final application shell.
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
