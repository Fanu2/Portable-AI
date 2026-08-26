from datetime import datetime

from portable_ai.models.runtime_health import (
    RuntimeHealth,
)

from portable_ai.gui.widgets.runtime_control_widget import (
    RuntimeControlWidget,
)


class FakeDashboardService:
    """
    Fake dashboard service for runtime control tests.
    """

    def runtime_names(
        self,
    ):

        return [
            "ollama",
        ]

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
            )

        return Snapshot()

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


def test_runtime_control_widget_displays_runtime(
    qtbot,
):

    widget = RuntimeControlWidget(
        FakeDashboardService()
    )

    qtbot.addWidget(
        widget
    )

    text = widget._label.text()

    assert "OLLAMA" in text
    assert "offline" in text
    assert "127.0.0.1:11434" in text
    assert "text_generation" in text


def test_runtime_control_widget_has_refresh_button(
    qtbot,
):

    widget = RuntimeControlWidget(
        FakeDashboardService()
    )

    qtbot.addWidget(
        widget
    )

    assert (
        widget._refresh_button.text()
        == "Refresh Health"
    )
