from pathlib import Path

from portable_ai.contracts.storage_manager import StorageManager


class StorageService:
    """
    Application service for Portable-AI storage.
    """

    def __init__(
        self,
        storage: StorageManager,
    ) -> None:
        self._storage = storage

    def root(self) -> Path:
        return self._storage.root()

    def models(self) -> Path:
        return self._storage.models_path()

    def data(self) -> Path:
        return self._storage.data_path()

    def config(self) -> Path:
        return self._storage.config_path()
