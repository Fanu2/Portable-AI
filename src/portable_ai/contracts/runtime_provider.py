from abc import ABC, abstractmethod
from typing import Any


class RuntimeProvider(ABC):
    """
    Abstract interface for AI inference runtimes.
    """

    @abstractmethod
    def discover(self) -> dict[str, Any]:
        """
        Discover available runtime capabilities.
        """
        pass

    @abstractmethod
    def capabilities(self) -> set[str]:
        """
        Return supported capabilities.
        """
        pass

    @abstractmethod
    def metadata(self) -> dict[str, Any]:
        """
        Return runtime metadata.
        """
        pass

    @abstractmethod
    def load_model(self, model_id: str) -> bool:
        """
        Load a model into the runtime.
        """
        pass

    @abstractmethod
    def unload_model(self, model_id: str) -> bool:
        """
        Unload a model from the runtime.
        """
        pass

    @abstractmethod
    def generate(self, prompt: str, **kwargs: Any) -> str:
        """
        Generate text output.
        """
        pass

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """
        Generate embeddings.
        """
        pass

    @abstractmethod
    def health(self) -> bool:
        """
        Check runtime availability.
        """
        pass
