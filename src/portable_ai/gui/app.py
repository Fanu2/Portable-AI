import os

# Force Qt to use X11 backend on Linux systems.
# Keeps GUI startup predictable on MX Linux.
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

from portable_ai.gui.ui_factory import (
    UIFactory,
)


def run() -> None:
    """
    Starts the Portable-AI GUI application.

    Startup flow:

        ApplicationFactory
                |
                ▼
        ApplicationContext
                |
                ▼
        UIFactory
                |
                ▼
        UIContext
                |
                ▼
        MainWindow
                |
                ▼
        ApplicationShellWidget

    Core services and GUI services remain separated.
    """

    #
    # Create Qt application instance.
    #
    app = QApplication(
        sys.argv
    )

    #
    # Locate project root.
    #
    root = (
        Path(__file__)
        .resolve()
        .parents[3]
    )

    #
    # Create core application context.
    #
    # Contains:
    #   - runtime services
    #   - model services
    #   - execution services
    #   - hardware services
    #
    context = ApplicationFactory(
        root
    ).create()

    #
    # Create GUI service context.
    #
    # UI services remain outside
    # ApplicationContext.
    #
    # This keeps GUI growth isolated
    # from core services.
    #
    active_execution = getattr(
        context,
        "active_execution",
        None,
    )

    ui_context = UIFactory().create(
        active_execution
    )

    #
    # Create main application window.
    #
    # Receives:
    #   - ApplicationContext
    #   - UIContext
    #
    window = MainWindow(
        context,
        ui_context,
    )

    window.resize(
        1000,
        700,
    )

    window.show()

    #
    # Start Qt event loop.
    #
    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    run()
