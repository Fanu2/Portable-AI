from portable_ai.gui.widgets.assistant.workspace_status_widget import (
    WorkspaceStatusWidget,
)


class FakeWorkspace:

    workspace_id = "demo"


class FakeAssistant:

    def workspace_context(
        self,
    ):

        return FakeWorkspace()


def test_workspace_status_widget_displays_workspace(
    qtbot,
):

    widget = WorkspaceStatusWidget(
        FakeAssistant()
    )

    qtbot.addWidget(
        widget
    )

    assert (
        "demo"
        in widget._workspace_label.text()
    )
