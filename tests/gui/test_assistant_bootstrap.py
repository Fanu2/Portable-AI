from portable_ai.gui.ui_factory import (
    UIFactory,
)


class FakeActiveExecution:
    """
    Fake execution boundary.

    Still required by UIFactory,
    but assistant UI no longer calls it
    directly.
    """

    def execute(
        self,
        prompt,
    ):

        return "execution response"


def test_bootstrap_creates_assistant_ui_context():
    """
    Verify UIFactory exposes assistant UI.
    """

    ui_context = UIFactory().create(
        FakeActiveExecution()
    )

    assert (
        ui_context.assistant
        is not None
    )


def test_bootstrap_assistant_stores_message():
    """
    Verify assistant UI forwards messages
    into the assistant service boundary.
    """

    ui_context = UIFactory().create(
        FakeActiveExecution()
    )

    result = (
        ui_context.assistant.send_message(
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
