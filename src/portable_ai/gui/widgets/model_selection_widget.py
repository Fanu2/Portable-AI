from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from portable_ai.contracts.active_model import (
    ActiveModel,
)


class ModelSelectionWidget(QWidget):
    """
    Allows selecting the active model.

    This widget only changes active model state.
    It does not execute models.
    """

    def __init__(
        self,
        inventory_service,
        active_model_service,
        runtime_name="ollama",
    ) -> None:

        super().__init__()

        self._inventory = inventory_service

        self._active_model = (
            active_model_service
        )

        self._runtime_name = runtime_name

        self._models = []

        self._label = QLabel(
            "Model Selection"
        )

        self._selector = QComboBox()

        self._activate_button = QPushButton(
            "Activate"
        )

        self._activate_button.clicked.connect(
            self.activate
        )

        layout = QVBoxLayout()

        layout.addWidget(
            self._label
        )

        layout.addWidget(
            self._selector
        )

        layout.addWidget(
            self._activate_button
        )

        self.setLayout(
            layout
        )

        self.refresh()

    def refresh(
        self,
    ) -> None:

        self._selector.clear()

        self._models = (
            self._inventory.all()
        )

        for model in self._models:

            self._selector.addItem(
                model.model_name
            )

    def activate(
        self,
    ) -> None:

        index = (
            self._selector.currentIndex()
        )

        if index < 0:
            return

        model = (
            self._models[index]
        )

        self._active_model.set_active_model(
            ActiveModel(
                model_name=model.model_name,
                runtime_name=self._runtime_name,
            )
        )
