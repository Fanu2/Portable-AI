from pathlib import Path

from portable_ai.contracts.storage_manager import StorageManager


class LocalStorageManager(StorageManager):
    """
    Local filesystem storage implementation.
    """

    def __init__(self, root: Path) -> None:
        self._root = root

    def initialize(self) -> None:
        for path in (
            self.models_path(),
            self.data_path(),
            self.config_path(),
            self.cache_path(),
            self.logs_path(),
        ):
            path.mkdir(
                parents=True,
                exist_ok=True,
            )

    def root(self) -> Path:
        return self._root

    def models_path(self) -> Path:
        return self._root / "models"

    def data_path(self) -> Path:
        return self._root / "data"

    def config_path(self) -> Path:
        return self._root / "config"

    def cache_path(self) -> Path:
        return self._root / "cache"

    def logs_path(self) -> Path:
        return self._root / "logs"
