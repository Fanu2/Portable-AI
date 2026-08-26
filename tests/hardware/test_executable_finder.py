from portable_ai.hardware.executable_finder import ExecutableFinder


def test_finds_existing_executable():
    finder = ExecutableFinder()

    result = finder.find("sh")

    assert result is not None


def test_returns_none_for_missing_executable():
    finder = ExecutableFinder()

    result = finder.find("portable-ai-definitely-does-not-exist")

    assert result is None
