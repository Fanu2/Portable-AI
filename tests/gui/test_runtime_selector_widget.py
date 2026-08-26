from portable_ai.gui.widgets.runtime_selector_widget import (
    RuntimeSelectorWidget,
)


def test_runtime_selector_widget_selects_runtime(qtbot):
    widget = RuntimeSelectorWidget(
        [
            "ollama",
            "lmstudio",
        ]
    )

    qtbot.addWidget(
        widget
    )

    assert (
        widget.selected_runtime()
        == "ollama"
    )
