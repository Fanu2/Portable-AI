from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ModelManagementWidget(QWidget):
    """
    Displays model management information.
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

        self._hardware = (
            hardware_service
        )

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

        for model in models:

            text += (
                f"{model.model_name}\n"
                f"Format: {model.format}\n"
                f"Size: {model.size_gb} GB\n"
                f"Installed: "
                f"{'Yes' if model.installed else 'No'}\n"
            )

            if self._compatibility is not None:

                text += (
                    "Compatibility: "
                    "Checked\n"
                )

            text += "\n"

        if not models:

            text += (
                "No models available\n"
            )

        self._label.setText(
            text
        )
