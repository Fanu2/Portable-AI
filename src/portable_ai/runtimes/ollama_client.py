from typing import Any

from portable_ai.runtimes.http_transport import (
    HttpTransport,
)


class OllamaClient:
    """
    Client boundary for Ollama API communication.
    """

    def __init__(
        self,
        transport: HttpTransport,
        endpoint: str = "http://127.0.0.1:11434",
    ) -> None:
        self._transport = transport
        self._endpoint = endpoint

    def endpoint(self) -> str:
        return self._endpoint

    def health(self) -> bool:
        try:
            self._transport.get(
                f"{self._endpoint}/api/tags"
            )
            return True

        except Exception:
            return False

    def list_models(self) -> list[str]:
        response = self._transport.get(
            f"{self._endpoint}/api/tags"
        )

        models = response.get(
            "models",
            [],
        )

        return [
            model["name"]
            for model in models
            if "name" in model
        ]

    def generate(
        self,
        prompt: str,
        **kwargs: Any,
    ) -> str:
        response = self._transport.post(
            f"{self._endpoint}/api/generate",
            {
                "prompt": prompt,
                **kwargs,
            },
        )

        return response.get(
            "response",
            "",
        )

    def embed(
        self,
        text: str,
    ) -> list[float]:
        response = self._transport.post(
            f"{self._endpoint}/api/embed",
            {
                "input": text,
            },
        )

        embeddings = response.get(
            "embeddings",
            [],
        )

        if not embeddings:
            return []

        return embeddings[0]
