from portable_ai.gui.widgets.model_selection_widget import (
    ModelSelectionWidget,
)


class FakeModel:

    model_name = "Qwen3.5-4B"


class FakeInventory:

    def all(self):

        return [
            FakeModel()
        ]


class FakeActiveModel:

    def __init__(self):

        self.selected = None

    def set_active_model(
        self,
        model,
    ):

        self.selected = model


def test_model_selection_widget_activates_model(
    qtbot,
):

    service = FakeActiveModel()

    widget = ModelSelectionWidget(
        FakeInventory(),
        service,
    )

    qtbot.addWidget(
        widget
    )

    widget.activate()

    assert service.selected is not None

    assert (
        service.selected.model_name
        == "Qwen3.5-4B"
    )
