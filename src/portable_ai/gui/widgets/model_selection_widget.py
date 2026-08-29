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
        - filter models for the selected runtime
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
        model_query_service,
        active_model_service,
        runtime_name="ollama",
        on_activated=None,
    ) -> None:

        super().__init__()

        #
        # Service dependencies.
        #
        self._model_query = (
            model_query_service
        )

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
        self._on_activated = (
            on_activated
        )

        #
        # Current model snapshot.
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

    def set_runtime(
        self,
        runtime_name: str,
    ) -> None:
        """
        Update the runtime used for
        model selection and activation.
        """

        self._runtime_name = runtime_name

        self.refresh()

    def refresh(
        self,
    ) -> None:
        """
        Refresh available model list for
        the currently selected runtime.
        """

        self._selector.clear()

        all_models = (
            self._model_query.all_models()
        )

        self._models = [
            model
            for model in all_models
            if (
                model.source_runtime
                in (
                    None,
                    self._runtime_name,
                )
            )
        ]

        for model in self._models:

            self._selector.addItem(
                model.name
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
                model_name=model.name,
                runtime_name=self._runtime_name,
            )
        )

        #
        # Notify parent UI.
        #
        if self._on_activated is not None:

            self._on_activated()
