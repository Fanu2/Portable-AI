from PySide6.QtWidgets import (
    QLabel,
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
        context=None,
        title: str = "Portable-AI",
    ) -> None:

        super().__init__()

        print("MAIN WINDOW: init")

        self._context = context

        self.setWindowTitle(
            title
        )

        self.resize(
            1000,
            700,
        )

        self._dashboard_widget = None

        self._setup_dashboard()

        print(
            "MAIN WINDOW: showing"
        )

        self.show()

        print(
            "MAIN WINDOW: shown"
        )

    def _setup_dashboard(
        self,
    ) -> None:

        print(
            "DASHBOARD SETUP START"
        )

        if self._context is None:

            print(
                "NO CONTEXT"
            )

            self.setCentralWidget(
                QLabel(
                    "Portable-AI"
                )
            )

            return

        print(
            "CONTEXT FOUND"
        )

        if hasattr(
            self._context,
            "dashboard",
        ):

            print(
                "CREATING DASHBOARD WIDGET"
            )

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

            print(
                "DASHBOARD CREATED"
            )

        else:

            print(
                "CREATING SERVICE DASHBOARD"
            )

            self._dashboard_widget = (
                DashboardWidget(
                    self._context
                )
            )

            print(
                "SERVICE DASHBOARD CREATED"
            )

        self.setCentralWidget(
            self._dashboard_widget
        )

        print(
            "CENTRAL WIDGET SET"
        )
