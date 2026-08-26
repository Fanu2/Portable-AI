from portable_ai.gui.widgets.runtime_details_widget import (
    RuntimeDetailsWidget,
)


def test_runtime_details_widget_displays_details(qtbot):
    widget = RuntimeDetailsWidget(
        "ollama",
        {
            "health": "offline",
            "endpoint": "127.0.0.1:11434",
            "capabilities": [
                "text_generation",
            ],
        },
    )

    qtbot.addWidget(
        widget
    )

    text = widget._label.text()

    assert "OLLAMA" in text
    assert "OFFLINE" in text
    assert "127.0.0.1:11434" in text
    assert "text_generation" in text


def test_runtime_details_widget_refresh_updates_health(qtbot):
    widget = RuntimeDetailsWidget(
        "ollama",
        {
            "health": "offline",
            "endpoint": "127.0.0.1:11434",
            "capabilities": [
                "text_generation",
            ],
        },
    )

    qtbot.addWidget(
        widget
    )

    widget.refresh(
        {
            "health": "online",
            "endpoint": "127.0.0.1:11434",
            "capabilities": [
                "text_generation",
            ],
        }
    )

    assert "ONLINE" in widget._label.text()
