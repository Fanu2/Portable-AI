from pathlib import Path

from portable_ai.storage.storage_manifest import (
    StorageManifest,
)


def test_storage_manifest_validates_layout(tmp_path):
    root = Path(tmp_path)

    for directory in (
        "models",
        "data",
        "config",
        "cache",
        "logs",
    ):
        (root / directory).mkdir()

    manifest = StorageManifest(root)

    assert manifest.is_valid()
    assert manifest.missing_directories() == []


def test_storage_manifest_detects_missing_directories(tmp_path):
    manifest = StorageManifest(
        Path(tmp_path)
    )

    assert not manifest.is_valid()
    assert "models" in manifest.missing_directories()
