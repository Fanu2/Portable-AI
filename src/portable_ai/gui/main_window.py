from PySide6.QtWidgets import (
    QMainWindow,
)

from portable_ai.gui.widgets.dashboard_widget import (
    DashboardWidget,
)


class MainWindow(QMainWindow):
    """
    Main Portable-AI application window.
    """

    def __init__(
        self,
        dashboard_service=None,
        title: str = "Portable-AI",
    ) -> None:
        super().__init__()

        self.setWindowTitle(
            title
        )

        if dashboard_service:
            self.setCentralWidget(
                DashboardWidget(
                    dashboard_service
                )
            )
