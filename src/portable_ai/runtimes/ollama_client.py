from typing import Any

from portable_ai.runtimes.http_transport import (
    HttpTransport,
)


class OllamaClient:
    """
    Client boundary for Ollama API communication.

    Responsibilities:
        - communicate with the Ollama HTTP API
        - check runtime health
        - discover installed models
        - generate text
        - generate embeddings

    The caller may provide a model for each
    generation request. Otherwise the client's
    configured default model is used.
    """

    def __init__(
        self,
        transport: HttpTransport,
        endpoint: str = "http://127.0.0.1:11434",
        model: str = "qwen3:4b",
    ) -> None:

        self._transport = transport
        self._endpoint = endpoint
        self._model = model

    def endpoint(
        self,
    ) -> str:
        """
        Return the Ollama endpoint.
        """

        return self._endpoint

    def health(
        self,
    ) -> bool:
        """
        Check whether Ollama is reachable.
        """

        try:

            self._transport.get(
                f"{self._endpoint}/api/tags"
            )

            return True

        except Exception:

            return False

    def list_models(
        self,
    ) -> list[str]:
        """
        Return installed Ollama model names.
        """

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
        model: str | None = None,
        **kwargs: Any,
    ) -> str:
        """
        Generate a response using Ollama.

        The supplied model takes priority over
        the configured default model.
        """

        selected_model = (
            model
            or self._model
        )

        payload = {
            "model": selected_model,
            "prompt": prompt,
            "stream": False,
            **kwargs,
        }

        response = self._transport.post(
            f"{self._endpoint}/api/generate",
            payload,
        )

        return response.get(
            "response",
            "",
        )

    def embed(
        self,
        text: str,
        model: str | None = None,
    ) -> list[float]:
        """
        Generate an embedding using Ollama.
        """

        selected_model = (
            model
            or self._model
        )

        response = self._transport.post(
            f"{self._endpoint}/api/embed",
            {
                "model": selected_model,
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
