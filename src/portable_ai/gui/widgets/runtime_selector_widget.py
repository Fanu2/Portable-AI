from PySide6.QtWidgets import (
    QComboBox,
    QVBoxLayout,
    QWidget,
)


class RuntimeSelectorWidget(QWidget):
    """
    Runtime selection control.
    """

    def __init__(
        self,
        runtimes: list[str],
    ) -> None:

        super().__init__()

        self._selector = QComboBox()

        self._selector.addItems(
            runtimes
        )

        layout = QVBoxLayout()

        layout.addWidget(
            self._selector
        )

        self.setLayout(
            layout
        )

    def selected_runtime(self) -> str:

        return self._selector.currentText()

    def on_changed(
        self,
        callback,
    ) -> None:

        self._selector.currentTextChanged.connect(
            callback
        )
