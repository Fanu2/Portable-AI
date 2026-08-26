from portable_ai.contracts.model_resource import (
    ModelResource,
)

from portable_ai.gui.widgets.model_inventory_widget import (
    ModelInventoryWidget,
)


class FakeModelInventoryService:
    """
    Fake model inventory service.
    """

    def available(
        self,
    ):

        return [
            ModelResource(
                model_name="Qwen3.5-4B",
                path="catalog://Qwen3.5-4B",
                size_gb=2.7,
                format="GGUF",
            ),
            ModelResource(
                model_name="nomic-embed-text",
                path="catalog://nomic-embed-text",
                size_gb=0.5,
                format="GGUF",
            ),
        ]


def test_model_inventory_widget_displays_models(
    qtbot,
):

    widget = ModelInventoryWidget(
        FakeModelInventoryService()
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
        "nomic-embed-text"
        in text
    )

    assert (
        "GGUF"
        in text
    )

    assert (
        "Available"
        in text
    )
