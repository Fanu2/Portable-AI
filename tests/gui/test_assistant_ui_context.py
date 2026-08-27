from portable_ai.gui.ui_factory import (
    UIFactory,
)


class FakeExecution:
    """
    Fake execution boundary.

    UIFactory still receives execution,
    but AssistantUIService no longer
    calls execution directly.
    """

    def execute(
        self,
        prompt,
    ):

        return "response"


def test_ui_context_exposes_assistant():

    context = UIFactory().create(
        FakeExecution()
    )

    assert (
        context.assistant
        is not None
    )


def test_assistant_ui_stores_message():

    context = UIFactory().create(
        FakeExecution()
    )

    result = (
        context.assistant
        .send_message(
            "hello"
        )
    )

    assert result is not None

    assert (
        result[0].content
        == "hello"
    )

    assert (
        result[0].sender
        == "user"
    )
