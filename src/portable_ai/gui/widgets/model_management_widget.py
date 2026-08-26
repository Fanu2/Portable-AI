from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ModelManagementWidget(QWidget):
    """
    Displays model management and compatibility information.
    """

    def __init__(
        self,
        inventory_service,
        compatibility_service=None,
        hardware_service=None,
    ) -> None:

        super().__init__()

        self._inventory = inventory_service

        self._compatibility = (
            compatibility_service
        )

        self._hardware = hardware_service

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

        models = (
            self._inventory.all()
        )

        text = (
            "Model Management\n"
            "----------------\n"
        )

        hardware = None

        if self._hardware is not None:

            hardware = (
                self._hardware.detect()
            )

        for model in models:

            text += (
                f"{model.model_name}\n"
                f"Format: {model.format}\n"
                f"Size: {model.size_gb} GB\n"
                f"Installed: "
                f"{'Yes' if model.installed else 'No'}\n"
            )

            if (
                self._compatibility is not None
                and hardware is not None
            ):

                compatible = (
                    self._compatibility.can_run(
                        model,
                        hardware,
                    )
                )

                text += (
                    "Compatibility: "
                    + (
                        "Ready"
                        if compatible
                        else "Not suitable"
                    )
                    + "\n"
                )

                minimum_ram = getattr(
                    model,
                    "minimum_ram_gb",
                    None,
                )

                if minimum_ram is not None:

                    text += (
                        f"RAM Required: "
                        f"{minimum_ram} GB\n"
                    )

                available_ram = getattr(
                    hardware,
                    "ram_gb",
                    None,
                )

                if available_ram is not None:

                    text += (
                        f"RAM Available: "
                        f"{available_ram} GB\n"
                    )

            text += "\n"

        if not models:

            text += (
                "No models available\n"
            )

        self._label.setText(
            text
        )
