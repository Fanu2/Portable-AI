from pathlib import Path

from portable_ai.storage.local_storage_manager import (
    LocalStorageManager,
)


def test_local_storage_manager_creates_structure(tmp_path):
    storage = LocalStorageManager(
        Path(tmp_path) / "Portable-AI"
    )

    storage.initialize()

    assert storage.root().exists()
    assert storage.models_path().exists()
    assert storage.data_path().exists()
    assert storage.config_path().exists()
    assert storage.cache_path().exists()
    assert storage.logs_path().exists()
