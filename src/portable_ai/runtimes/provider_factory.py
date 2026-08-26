from portable_ai.contracts.runtime_descriptor import RuntimeDescriptor
from portable_ai.runtimes.http_transport import HttpTransport
from portable_ai.runtimes.ollama_client import OllamaClient
from portable_ai.runtimes.ollama_provider import (
    OllamaRuntimeProvider,
)


class ProviderFactory:
    """
    Creates runtime providers from descriptors.
    """

    def create(
        self,
        descriptor: RuntimeDescriptor,
    ):
        if descriptor.name == "Ollama":
            client = OllamaClient(
                HttpTransport()
            )

            return OllamaRuntimeProvider(
                client
            )

        raise ValueError(
            f"Unsupported runtime: {descriptor.name}"
        )
