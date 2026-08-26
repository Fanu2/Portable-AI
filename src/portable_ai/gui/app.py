import os

os.environ.setdefault(
    "QT_QPA_PLATFORM",
    "xcb",
)

import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
)

from portable_ai.core.application_factory import (
    ApplicationFactory,
)

from portable_ai.gui.main_window import (
    MainWindow,
)


def run() -> None:
    """
    Starts the Portable-AI GUI application.
    """

    app = QApplication(
        sys.argv
    )

    root = (
        Path(__file__)
        .resolve()
        .parents[3]
    )

    context = ApplicationFactory(
        root
    ).create()

    window = MainWindow(
        context,
    )

    window.resize(
        1000,
        700,
    )

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    run()
