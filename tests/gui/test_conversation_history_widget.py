from dataclasses import dataclass

from portable_ai.gui.widgets.assistant.conversation_widget import (
    ConversationWidget,
)


@dataclass
class FakeMessage:

    sender: str

    content: str


class FakeAssistant:
    pass


def test_conversation_widget_loads_history(
    qtbot,
):

    widget = ConversationWidget(
        FakeAssistant()
    )

    qtbot.addWidget(
        widget
    )

    widget.load_history(
        [
            FakeMessage(
                "User",
                "Hello",
            ),

            FakeMessage(
                "Assistant",
                "Hi",
            ),
        ]
    )

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
