from portable_ai.gui.widgets.execution_panel_widget import (
    ExecutionPanelWidget,
)


class FakeExecution:

    def __init__(self):

        self.prompt = None

    def execute(
        self,
        prompt,
    ):

        self.prompt = prompt

        return "AI response"


def test_execution_panel_executes_prompt(
    qtbot,
):

    service = FakeExecution()

    widget = ExecutionPanelWidget(
        service
    )

    qtbot.addWidget(
        widget
    )

    widget._prompt.setText(
        "Hello"
    )

    widget.execute()

    assert (
        widget._result
        .toPlainText()
        == "AI response"
    )

    assert (
        service.prompt
        == "Hello"
    )
