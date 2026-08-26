from datetime import datetime

from portable_ai.models.runtime_health import (
    RuntimeHealth,
)

from portable_ai.gui.main_window import (
    MainWindow,
)


class FakeDashboardService:

    def summary(self):
        return {
            "runtimes": {
                "ollama": False
            },
            "available_runtime_count": 0,
        }

    def runtime_names(self):
        return [
            "ollama",
        ]

    def runtime_metadata(
        self,
        runtime_name,
    ):
        return {
            "endpoint": "127.0.0.1:11434",
            "capabilities": [
                "text_generation",
                "embeddings",
            ],
        }

    def runtime_health_snapshot(
        self,
        runtime_name,
    ):
        class Snapshot:
            health = RuntimeHealth.OFFLINE
            checked_at = datetime(
                2026,
                8,
                26,
                12,
                0,
                0,
            )

        return Snapshot()


def test_main_window_title(qtbot):
    window = MainWindow()

    qtbot.addWidget(
        window
    )

    assert (
        window.windowTitle()
        == "Portable-AI"
    )


def test_main_window_uses_dashboard_widget(qtbot):
    window = MainWindow(
        FakeDashboardService()
    )

    qtbot.addWidget(
        window
    )

    assert window.centralWidget() is not None
