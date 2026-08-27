from PySide6.QtWidgets import (
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from portable_ai.gui.widgets.execution_panel_widget import (
    ExecutionPanelWidget,
)

from portable_ai.gui.widgets.assistant.assistant_panel_widget import (
    AssistantPanelWidget,
)

from portable_ai.gui.widgets.assistant.workspace_status_widget import (
    WorkspaceStatusWidget,
)


class ApplicationShellWidget(QWidget):
    """
    Main GUI composition container.

    Combines:

        - Dashboard
        - Execution panel
        - Assistant panel
        - Workspace status

    Responsibilities:
        - compose GUI widgets
        - connect UI services to widgets
        - control visual layout only

    Does not:
        - manage execution logic
        - manage models
        - manage runtimes
        - manage assistant logic
        - manage workspace logic

    Keeps MainWindow lightweight.
    """

    def __init__(
        self,
        dashboard_widget,
        execution_service=None,
        assistant_service=None,
    ) -> None:

        super().__init__()

        self._execution_panel = None

        self._assistant_panel = None

        self._workspace_status = None

        layout = QVBoxLayout()

        #
        # Dashboard area.
        #
        # Dashboard can contain:
        #   - hardware
        #   - models
        #   - runtime information
        #
        # Keep it scrollable.
        #
        dashboard_scroll = QScrollArea()

        dashboard_scroll.setWidgetResizable(
            True
        )

        dashboard_scroll.setWidget(
            dashboard_widget
        )

        layout.addWidget(
            dashboard_scroll,
            2,
        )

        #
        # Execution UI.
        #
        # Controlled execution boundary.
        #
        if execution_service is not None:

            self._execution_panel = (
                ExecutionPanelWidget(
                    execution_service
                )
            )

            layout.addWidget(
                self._execution_panel,
                1,
            )

        #
        # Assistant UI.
        #
        # Conversation and assistant
        # interaction boundary.
        #
        if assistant_service is not None:

            self._assistant_panel = (
                AssistantPanelWidget(
                    assistant_service
                )
            )

            layout.addWidget(
                self._assistant_panel,
                2,
            )

            #
            # Workspace awareness.
            #
            # Displays workspace state only.
            #
            self._workspace_status = (
                WorkspaceStatusWidget(
                    assistant_service
                )
            )

            layout.addWidget(
                self._workspace_status,
                0,
            )

        #
        # Final shell layout.
        #
        self.setLayout(
            layout
        )
