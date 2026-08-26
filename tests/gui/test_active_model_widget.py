from portable_ai.contracts.active_model import (
    ActiveModel,
)

from portable_ai.gui.widgets.active_model_widget import (
    ActiveModelWidget,
)


class FakeActiveModelService:

    def get_active_model(
        self,
    ):

        return ActiveModel(
            model_name="Qwen3.5-4B",
            runtime_name="ollama",
            capability="text_generation",
        )


def test_active_model_widget_displays_selection(
    qtbot,
):

    widget = ActiveModelWidget(
        FakeActiveModelService()
    )

    qtbot.addWidget(
        widget
    )

    text = widget._label.text()

    assert (
        "Qwen3.5-4B"
        in text
    )

    assert (
        "ollama"
        in text
    )

    assert (
        "Selected"
        in text
    )
