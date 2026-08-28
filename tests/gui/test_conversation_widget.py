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
    """

    def __init__(
        self,
    ) -> None:

        self.message = None

        self.generate_called = False

        self._history = []

    def send_message(
        self,
        message: str,
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
    ) -> str:

        self.generate_called = True

        response = FakeMessage(
            "Assistant",
            "assistant response",
        )

        self._history.append(
            response
        )

        return (
            "assistant response"
        )


def test_conversation_widget_generates_response(
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

    assert (
        assistant.generate_called
        is True
    )

    assert (
        widget._input.text()
        == ""
    )
