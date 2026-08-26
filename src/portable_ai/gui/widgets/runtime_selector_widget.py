from PySide6.QtWidgets import (
    QComboBox,
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

    def selected_runtime(self) -> str:
        return self._selector.currentText()

    def on_changed(
        self,
        callback,
    ) -> None:
        self._selector.currentTextChanged.connect(
            callback
        )
