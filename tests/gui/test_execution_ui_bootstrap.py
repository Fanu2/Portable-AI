from portable_ai.gui.ui_factory import (
    UIFactory,
)


class FakeActiveExecution:
    """
    Fake backend execution service.
    """

    def execute(
        self,
        prompt,
    ):

        return "response"


def test_ui_factory_creates_execution_boundary():

    ui_context = UIFactory().create(
        FakeActiveExecution()
    )

    assert (
        ui_context.execution
        is not None
    )


def test_ui_execution_service_forwards_request():

    ui_context = UIFactory().create(
        FakeActiveExecution()
    )

    result = (
        ui_context.execution.execute(
            "hello"
        )
    )

    assert (
        result
        == "response"
    )
