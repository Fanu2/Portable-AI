from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class HardwareWidget(QWidget):
    """
    Displays local hardware information.
    """

    def __init__(
        self,
        hardware_service,
    ) -> None:

        super().__init__()

        self._service = hardware_service

        self._label = QLabel()

        layout = QVBoxLayout()

        layout.addWidget(
            self._label
        )

        self.setLayout(
            layout
        )

        self.refresh()

    def refresh(
        self,
    ) -> None:

        hardware = (
            self._service.detect()
        )

        self._label.setText(
            "Hardware\n"
            "----------------\n"
            f"CPU Cores: "
            f"{hardware.cpu_cores}\n"
            f"RAM: "
            f"{hardware.ram_gb} GB\n"
            f"Storage: "
            f"{hardware.storage_gb} GB"
        )
