from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ActiveModelWidget(QWidget):
    """
    Displays the currently selected active model.

    Responsibilities:
        - read active model state
        - render active model information
        - refresh when model state changes

    This widget does not:
        - select models
        - activate models
        - manage model state

    ActiveModelService remains the
    source of truth.
    """

    def __init__(
        self,
        active_model_service,
    ) -> None:

        super().__init__()

        #
        # Shared active model state.
        #
        self._service = (
            active_model_service
        )

        #
        # Display.
        #
        self._label = QLabel()

        layout = QVBoxLayout()

        layout.addWidget(
            self._label
        )

        self.setLayout(
            layout
        )

        #
        # Render initial state.
        #
        self.refresh()

    def refresh(
        self,
    ) -> None:
        """
        Refresh the displayed active model state.

        The widget always reads directly from
        ActiveModelService and therefore does
        not maintain its own model state.
        """

        active_model = (
            self._service
            .get_active_model()
        )

        self._label.setText(
            self._format_active_model(
                active_model
            )
        )

    def update_active_model(
        self,
    ) -> None:
        """
        Public notification hook.

        Call this after the active model state
        changes.

        Kept separate from refresh() so callers
        express their intent clearly.
        """

        self.refresh()

    def _format_active_model(
        self,
        active_model,
    ) -> str:
        """
        Format active model state for display.
        """

        text = (
            "Active Model\n"
            "----------------\n"
        )

        if active_model is None:

            return (
                text
                + "No model selected\n"
            )

        text += (
            f"Model: "
            f"{active_model.model_name}\n"
            f"Runtime: "
            f"{active_model.runtime_name}\n"
        )

        if active_model.capability:

            text += (
                f"Capability: "
                f"{active_model.capability}\n"
            )

        text += (
            "Status: Selected\n"
        )

        return text
