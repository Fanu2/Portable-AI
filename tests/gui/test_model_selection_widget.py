from portable_ai.gui.widgets.model_selection_widget import (
    ModelSelectionWidget,
)


class FakeModel:

    name = "Qwen3.5-4B"

    source_runtime = None


class FakeModelQueryService:

    def all_models(
        self,
    ):

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
        FakeModelQueryService(),
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
