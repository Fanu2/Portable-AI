from dataclasses import dataclass

from portable_ai.gui.widgets.assistant.conversation_widget import (
    ConversationWidget,
)


@dataclass
class Message:

    sender: str
    content: str


class FakeAssistant:

    def conversation_history(
        self,
    ):

        return [
            Message(
                "User",
                "Hello",
            ),
            Message(
                "Assistant",
                "Hi",
            ),
        ]

    def send_message(
        self,
        message,
    ):
        pass

    def generate_response(
        self,
    ):

        return "Hi"


def test_conversation_widget_refreshes_history(
    qtbot,
):

    widget = ConversationWidget(
        FakeAssistant()
    )

    qtbot.addWidget(
        widget
    )

    widget.refresh_history()

    text = (
        widget._display
        .toPlainText()
    )

    assert (
        "User: Hello"
        in text
    )

    assert (
        "Assistant: Hi"
        in text
    )
