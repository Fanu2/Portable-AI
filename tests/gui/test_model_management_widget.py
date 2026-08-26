from portable_ai.gui.widgets.model_management_widget import (
    ModelManagementWidget,
)


class FakeModel:

    model_name = "Qwen3.5-4B"
    format = "GGUF"
    size_gb = 2.7
    installed = False
    minimum_ram_gb = 4.0


class FakeInventoryService:

    def all(
        self,
    ):

        return [
            FakeModel()
        ]


class FakeHardware:

    ram_gb = 8.0


class FakeHardwareService:

    def detect(
        self,
    ):

        return FakeHardware()


class FakeCompatibilityService:

    def can_run(
        self,
        model,
        hardware,
    ):

        return (
            hardware.ram_gb
            >= model.minimum_ram_gb
        )


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


def test_model_management_widget_displays_compatibility(
    qtbot,
):

    widget = ModelManagementWidget(
        FakeInventoryService(),
        FakeCompatibilityService(),
        FakeHardwareService(),
    )

    qtbot.addWidget(
        widget
    )

    text = widget._label.text()

    assert (
        "Compatibility: Ready"
        in text
    )

    assert (
        "RAM Required: 4.0 GB"
        in text
    )

    assert (
        "RAM Available: 8.0 GB"
        in text
    )
