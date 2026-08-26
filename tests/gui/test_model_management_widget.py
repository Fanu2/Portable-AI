from portable_ai.gui.widgets.model_management_widget import (
    ModelManagementWidget,
)


class FakeModel:

    model_name = "Qwen3.5-4B"
    format = "GGUF"
    size_gb = 2.7
    installed = False


class FakeInventoryService:

    def all(
        self,
    ):

        return [
            FakeModel()
        ]


def test_model_management_widget_displays_model(
    qtbot,
):

    widget = ModelManagementWidget(
        FakeInventoryService()
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
        "GGUF"
        in text
    )

    assert (
        "Installed: No"
        in text
    )
