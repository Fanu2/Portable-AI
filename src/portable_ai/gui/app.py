import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from portable_ai.core.application_factory import (
    ApplicationFactory,
)
from portable_ai.gui.main_window import (
    MainWindow,
)


def run() -> None:
    app = QApplication(
        sys.argv
    )

    context = ApplicationFactory(
        Path.cwd()
    ).create()

    window = MainWindow(
        context.dashboard
    )

    window.show()

    sys.exit(
        app.exec()
    )
