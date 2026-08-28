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
    Start the Portable-AI GUI application.

    Startup flow:

        ApplicationFactory
                |
                ▼
        ApplicationContext
                |
                ├──────────────► active execution
                │
                └──────────────► configured assistant
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

    Core composition remains inside
    ApplicationFactory.

    GUI composition remains inside
    UIFactory.

    The GUI does not construct:
        - runtimes
        - providers
        - models
        - assistant generation backends
    """

    #
    # Create Qt application.
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
    # Create application context.
    #
    # ApplicationFactory owns core
    # dependency composition.
    #
    context = (
        ApplicationFactory(
            root
        ).create()
    )

    #
    # Extract GUI-facing dependencies.
    #
    active_execution = getattr(
        context,
        "active_execution",
        None,
    )

    #
    # Use the assistant configured by
    # ApplicationFactory.
    #
    assistant_service = getattr(
        context,
        "assistant_service",
        None,
    )

    #
    # Create GUI service context.
    #
    ui_context = (
        UIFactory()
        .create(
            active_execution,
            assistant_service=assistant_service,
        )
    )

    #
    # Create main application window.
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
