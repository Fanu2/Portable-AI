from pathlib import Path

from portable_ai.config.local_config_manager import (
    LocalConfigManager,
)


def test_local_config_save_and_load(tmp_path):
    config_file = (
        Path(tmp_path)
        / "config"
        / "portable-ai.json"
    )

    manager = LocalConfigManager(
        config_file
    )

    data = {
        "runtime": "Ollama",
        "offline": True,
    }

    manager.save(data)

    loaded = manager.load()

    assert loaded == data
    assert manager.config_path() == config_file
