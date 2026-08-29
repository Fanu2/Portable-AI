from typing import Any

from portable_ai.contracts.runtime_provider import (
    RuntimeProvider,
)


class HuggingFaceRuntimeProvider(RuntimeProvider):
    """
    Runtime provider adapter for local
    Hugging Face model execution.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def discover(self) -> dict[str, Any]:
        return {
            "models": [
                self._client.model()
            ],
        }

    def capabilities(self) -> set[str]:
        return {
            "text_generation",
        }

    def metadata(self) -> dict[str, Any]:
        return {
            "model": self._client.model(),
            "capabilities": [
                "text_generation",
            ],
        }

    def load_model(
        self,
        model_id: str,
    ) -> bool:

        self._client.load()

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

        return []

    def health(self) -> bool:

        return self._client.health()
