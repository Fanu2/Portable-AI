from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ActiveModelWidget(QWidget):
    """
    Displays currently selected active model.
    """

    def __init__(
        self,
        active_model_service,
    ) -> None:

        super().__init__()

        self._service = (
            active_model_service
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

        active_model = (
            self._service
            .get_active_model()
        )

        text = (
            "Active Model\n"
            "----------------\n"
        )

        if active_model is None:

            text += (
                "No model selected\n"
            )

        else:

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

        self._label.setText(
            text
        )
