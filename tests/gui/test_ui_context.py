from portable_ai.gui.ui_factory import (
    UIFactory,
)


class FakeActiveExecution:

    def execute(
        self,
        prompt,
    ):

        return "ok"


def test_ui_context_creates_execution_service():

    context = UIFactory().create(
        FakeActiveExecution()
    )

    assert (
        context.execution
        is not None
    )
