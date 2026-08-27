from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class WorkspaceStatusWidget(QWidget):
    """
    Workspace status display.

    Responsibilities:
        - display workspace state
        - show assistant workspace context
        - refresh workspace information

    Does not:
        - modify workspace
        - load documents
        - perform retrieval
        - manage storage

    Workspace state ownership remains
    inside AssistantService.
    """

    def __init__(
        self,
        assistant_ui_service,
    ) -> None:

        super().__init__()

        #
        # GUI-facing assistant boundary.
        #
        # Widget only reads workspace
        # information through the service.
        #
        self._assistant = (
            assistant_ui_service
        )

        self._workspace_label = QLabel()

        layout = QVBoxLayout()

        layout.addWidget(
            self._workspace_label
        )

        self.setLayout(
            layout
        )

        #
        # Initial state load.
        #
        self.refresh()

    def refresh(
        self,
    ) -> None:
        """
        Refresh workspace display.

        Flow:

            WorkspaceStatusWidget
                    |
                    ▼
            AssistantUIService
                    |
                    ▼
            AssistantService
                    |
                    ▼
            WorkspaceContext

        The widget only renders state.
        """

        workspace = (
            self._assistant
            .workspace_context()
        )

        workspace_id = (
            workspace.workspace_id
            or "No workspace"
        )

        self._workspace_label.setText(
            f"Workspace: {workspace_id}"
        )
