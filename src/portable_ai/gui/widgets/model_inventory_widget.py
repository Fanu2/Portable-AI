from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ModelInventoryWidget(QWidget):
    """
    Displays available local models.
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

        models = (
            self._service.available()
        )

        text = (
            "Models\n"
            "----------------\n"
        )

        for model in models:

            text += (
                f"{model.model_name}\n"
                f"Format: {model.format}\n"
                f"Size: {model.size_gb} GB\n"
                f"Status: Available\n\n"
            )

        self._label.setText(
            text
        )
