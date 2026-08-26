from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)

from portable_ai.gui.widgets.hardware_widget import (
    HardwareWidget,
)


class FakeHardwareService:

    def detect(
        self,
    ):

        return HardwareInfo(
            cpu_cores=8,
            ram_gb=16.0,
            storage_gb=1000.0,
        )


def test_hardware_widget_displays_information(
    qtbot,
):

    widget = HardwareWidget(
        FakeHardwareService()
    )

    qtbot.addWidget(
        widget
    )

    text = widget._label.text()

    assert (
        "CPU Cores: 8"
        in text
    )

    assert (
        "RAM: 16.0 GB"
        in text
    )

    assert (
        "Storage: 1000.0 GB"
        in text
    )
