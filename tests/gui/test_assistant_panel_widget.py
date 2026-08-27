from portable_ai.gui.widgets.assistant.assistant_panel_widget import (
    AssistantPanelWidget,
)


class FakeAssistant:

    def send_message(
        self,
        message,
    ):

        return "response"


def test_assistant_panel_creates(
    qtbot,
):

    widget = AssistantPanelWidget(
        FakeAssistant()
    )

    qtbot.addWidget(
        widget
    )

    assert widget is not None
