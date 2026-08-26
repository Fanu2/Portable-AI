from typing import Any

from portable_ai.contracts.runtime_provider import (
    RuntimeProvider,
)


class OllamaRuntimeProvider(RuntimeProvider):
    """
    Runtime provider adapter for Ollama.
    """

    def __init__(
        self,
        client,
    ) -> None:
        self._client = client

    def discover(self) -> dict[str, Any]:
        return {
            "models": self._client.list_models(),
        }

    def capabilities(self) -> set[str]:
        return {
            "text_generation",
            "embeddings",
        }

    def metadata(self) -> dict[str, Any]:
        return {
            "endpoint": self._client.endpoint(),
            "capabilities": [
                "text_generation",
                "embeddings",
            ],
        }

    def load_model(
        self,
        model_id: str,
    ) -> bool:
        return True

    def unload_model(
        self,
        model_id: str,
    ) -> bool:
        return True

    def generate(
        self,
        prompt: str,
        **kwargs: Any,
    ) -> str:
        return self._client.generate(
            prompt,
            **kwargs,
        )

    def embed(
        self,
        text: str,
    ) -> list[float]:
        return self._client.embed(
            text
        )

    def health(self) -> bool:
        return self._client.health()
