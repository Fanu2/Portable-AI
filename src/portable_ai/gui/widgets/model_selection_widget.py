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

    Responsibilities:
        - display available models
        - allow model selection
        - update active model state
        - notify the parent UI after activation

    Does not:
        - execute models
        - manage runtimes
        - manage model inventory
        - own active model state
    """

    def __init__(
        self,
        inventory_service,
        active_model_service,
        runtime_name="ollama",
        on_activated=None,
    ) -> None:

        super().__init__()

        #
        # Service dependencies.
        #
        self._inventory = inventory_service

        self._active_model = (
            active_model_service
        )

        #
        # Runtime associated with
        # selected models.
        #
        self._runtime_name = runtime_name

        #
        # Optional UI callback.
        #
        # Called after successful model
        # activation so parent widgets
        # can refresh their display.
        #
        self._on_activated = (
            on_activated
        )

        #
        # Current inventory snapshot.
        #
        self._models = []

        #
        # UI elements.
        #
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

        #
        # Layout.
        #
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

        #
        # Load available models.
        #
        self.refresh()

    def refresh(
        self,
    ) -> None:
        """
        Refresh available model list.
        """

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
        """
        Activate the currently selected model.

        Active model state remains owned
        by ActiveModelService.
        """

        index = (
            self._selector.currentIndex()
        )

        if index < 0:

            return

        if index >= len(
            self._models
        ):

            return

        model = (
            self._models[index]
        )

        #
        # Update application state.
        #
        self._active_model.set_active_model(
            ActiveModel(
                model_name=model.model_name,
                runtime_name=self._runtime_name,
            )
        )

        #
        # Notify parent UI.
        #
        # This allows the active model
        # display to refresh immediately
        # without this widget knowing
        # about dashboard internals.
        #
        if self._on_activated is not None:

            self._on_activated()
