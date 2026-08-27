from PySide6.QtWidgets import (
    QLabel,
)

from portable_ai.gui.widgets.application_shell_widget import (
    ApplicationShellWidget,
)


class FakeDashboard(
    QLabel
):
    """
    Minimal QWidget replacement
    for dashboard testing.
    """

    def __init__(
        self,
    ) -> None:

        super().__init__(
            "Dashboard"
        )


class FakeExecution:
    """
    Fake execution UI service.
    """

    def execute(
        self,
        prompt,
    ):

        return "ok"


def test_application_shell_creates_dashboard(
    qtbot,
):

    widget = ApplicationShellWidget(
        FakeDashboard()
    )

    qtbot.addWidget(
        widget
    )

    assert widget is not None
