from datetime import datetime

from portable_ai.models.runtime_health import (
    RuntimeHealth,
)

from portable_ai.gui.widgets.dashboard_widget import (
    DashboardWidget,
)


class FakeDashboardService:

    def summary(self):
        return {
            "runtimes": {
                "ollama": False,
                "test-runtime": False,
            },
            "available_runtime_count": 0,
        }

    def runtime_names(self):
        return [
            "ollama",
            "test-runtime",
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


def test_dashboard_widget_displays_runtime_status(qtbot):
    widget = DashboardWidget(
        FakeDashboardService()
    )

    qtbot.addWidget(
        widget
    )

    assert (
        "OLLAMA"
        in widget._runtime_label.text()
    )

    assert (
        "Offline"
        in widget._runtime_label.text()
    )


def test_dashboard_widget_has_refresh_button(qtbot):
    widget = DashboardWidget(
        FakeDashboardService()
    )

    qtbot.addWidget(
        widget
    )

    assert (
        widget._refresh_button.text()
        == "Refresh"
    )


def test_dashboard_widget_shows_runtime_details(qtbot):
    widget = DashboardWidget(
        FakeDashboardService()
    )

    qtbot.addWidget(
        widget
    )

    assert widget._details is not None

    text = widget._details._label.text()

    assert "OLLAMA" in text
    assert "127.0.0.1:11434" in text
    assert "text_generation" in text
    assert "OFFLINE" in text
    assert "Checked:" in text


def test_dashboard_widget_has_runtime_selector(qtbot):
    widget = DashboardWidget(
        FakeDashboardService()
    )

    qtbot.addWidget(
        widget
    )

    assert (
        widget._selector.selected_runtime()
        == "ollama"
    )


def test_dashboard_widget_supports_multiple_runtimes(qtbot):
    widget = DashboardWidget(
        FakeDashboardService()
    )

    qtbot.addWidget(
        widget
    )

    assert (
        widget._selector._selector.count()
        == 2
    )


def test_dashboard_widget_displays_health_timestamp(qtbot):
    widget = DashboardWidget(
        FakeDashboardService()
    )

    qtbot.addWidget(
        widget
    )

    text = widget._details._label.text()

    assert (
        "Checked:"
        in text
    )

    assert (
        "2026"
        in text
    )
