from portable_ai.gui import app


def test_gui_run_exists():

    assert callable(
        app.run
    )
