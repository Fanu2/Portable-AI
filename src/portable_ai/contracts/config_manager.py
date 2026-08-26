from abc import ABC, abstractmethod
from pathlib import Path


class ConfigManager(ABC):
    """
    Abstract interface for Portable-AI configuration.
    """

    @abstractmethod
    def config_path(self) -> Path:
        raise NotImplementedError

    @abstractmethod
    def load(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def save(self, config: dict) -> None:
        raise NotImplementedError
