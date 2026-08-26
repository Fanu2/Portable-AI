from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ModelInventoryWidget(QWidget):
    """
    Displays available model inventory.
    """

    def __init__(
        self,
        inventory_service,
    ) -> None:

        super().__init__()

        self._service = inventory_service

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

        if hasattr(
            self._service,
            "all",
        ):

            models = (
                self._service.all()
            )

        else:

            models = (
                self._service.available()
            )

        text = (
            "Models\n"
            "----------------\n"
        )

        for model in models:

            installed = (
                "Yes"
                if getattr(
                    model,
                    "installed",
                    False,
                )
                else "No"
            )

            text += (
                f"{model.model_name}\n"
                f"Format: {model.format}\n"
                f"Size: {model.size_gb} GB\n"
                f"Installed: {installed}\n"
                "Status: Available\n"
            )

            path = getattr(
                model,
                "path",
                None,
            )

            if path:

                text += (
                    f"Path: {path}\n"
                )

            text += "\n"

        if not models:

            text += (
                "No models detected\n"
            )

        self._label.setText(
            text
        )
