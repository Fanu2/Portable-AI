from abc import ABC, abstractmethod
from pathlib import Path


class StorageManager(ABC):
    """
    Abstract interface for Portable-AI storage.
    """

    @abstractmethod
    def root(self) -> Path:
        """
        Return Portable-AI root directory.
        """
        raise NotImplementedError

    @abstractmethod
    def models_path(self) -> Path:
        """
        Return models directory.
        """
        raise NotImplementedError

    @abstractmethod
    def data_path(self) -> Path:
        """
        Return user data directory.
        """
        raise NotImplementedError

    @abstractmethod
    def config_path(self) -> Path:
        """
        Return configuration directory.
        """
        raise NotImplementedError
