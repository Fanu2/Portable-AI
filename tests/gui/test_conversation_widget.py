from dataclasses import dataclass

from portable_ai.gui.widgets.assistant.conversation_widget import (
    ConversationWidget,
)


@dataclass
class FakeMessage:

    sender: str

    content: str


class FakeAssistant:
    """
    Fake AssistantUIService.

    Provides:
        - message forwarding
        - conversation state
        - response generation
    """

    def __init__(
        self,
    ) -> None:

        self.message = None

        self._history = []

    def send_message(
        self,
        message,
    ) -> None:

        self.message = message

        self._history.append(
            FakeMessage(
                "User",
                message,
            )
        )

    def conversation_history(
        self,
    ):

        return self._history

    def generate_response(
        self,
    ):

        response = FakeMessage(
            "Assistant",
            "assistant response",
        )

        self._history.append(
            response
        )

        return "assistant response"


def test_conversation_widget_renders_response(
    qtbot,
):

    assistant = FakeAssistant()

    widget = ConversationWidget(
        assistant
    )

    qtbot.addWidget(
        widget
    )

    widget._input.setText(
        "Hello"
    )

    widget._send_message()

    text = (
        widget._display
        .toPlainText()
    )

    assert (
        "User: Hello"
        in text
    )

    assert (
        "Assistant: assistant response"
        in text
    )

    assert (
        assistant.message
        == "Hello"
    )
