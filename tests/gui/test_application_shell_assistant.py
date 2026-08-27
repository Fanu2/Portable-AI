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
    Minimal dashboard widget.
    """

    def __init__(
        self,
    ) -> None:

        super().__init__(
            "Dashboard"
        )


class FakeWorkspace:
    """
    Minimal workspace context.
    """

    workspace_id = "demo"


class FakeAssistant:
    """
    Fake assistant UI service.

    Provides:
        - assistant panel contract
        - workspace context contract
    """

    def send_message(
        self,
        message,
    ):

        return "response"

    def generate_response(
        self,
    ):

        return "assistant response"

    def conversation_history(
        self,
    ):

        return []

    def workspace_context(
        self,
    ):

        return FakeWorkspace()


def test_application_shell_accepts_assistant(
    qtbot,
):

    widget = ApplicationShellWidget(
        FakeDashboard(),
        assistant_service=FakeAssistant(),
    )

    qtbot.addWidget(
        widget
    )

    assert (
        widget._assistant_panel
        is not None
    )

    assert (
        widget._workspace_status
        is not None
    )
