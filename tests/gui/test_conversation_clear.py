from portable_ai.gui.widgets.assistant.conversation_widget import (
    ConversationWidget,
)


class FakeAssistant:

    def __init__(
        self,
    ) -> None:

        self.cleared = False

    def clear(
        self,
    ):

        self.cleared = True


def test_conversation_widget_clears_session(
    qtbot,
):

    assistant = FakeAssistant()

    widget = ConversationWidget(
        assistant
    )

    qtbot.addWidget(
        widget
    )

    widget._display.append(
        "User: Hello"
    )

    widget.clear_session()

    assert (
        assistant.cleared
        is True
    )

    assert (
        widget._display
        .toPlainText()
        == ""
    )
