from portable_ai.gui.app import run


def test_app_entry_exists():
    assert callable(run)
