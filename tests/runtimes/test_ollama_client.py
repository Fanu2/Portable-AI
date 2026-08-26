from portable_ai.runtimes.ollama_client import OllamaClient


class FakeTransport:
    def get(self, url):
        return {
            "models": []
        }

    def post(self, url, data):
        return {
            "response": "hello from ollama"
        }


class FailingTransport:
    def get(self, url):
        raise RuntimeError()

    def post(self, url, data):
        raise RuntimeError()


def test_ollama_client_endpoint():
    client = OllamaClient(
        FakeTransport()
    )

    assert (
        client.endpoint()
        == "http://127.0.0.1:11434"
    )


def test_ollama_client_health_success():
    client = OllamaClient(
        FakeTransport()
    )

    assert client.health()


def test_ollama_client_health_failure():
    client = OllamaClient(
        FailingTransport()
    )

    assert not client.health()


def test_ollama_client_lists_models():
    class ModelTransport:
        def get(self, url):
            return {
                "models": [
                    {"name": "qwen3:4b"},
                    {"name": "nomic-embed-text"},
                ]
            }

    client = OllamaClient(
        ModelTransport()
    )

    assert client.list_models() == [
        "qwen3:4b",
        "nomic-embed-text",
    ]


def test_ollama_client_generate():
    client = OllamaClient(
        FakeTransport()
    )

    result = client.generate(
        "hello"
    )

    assert result == "hello from ollama"


def test_ollama_client_embed():
    class EmbedTransport:
        def post(self, url, data):
            return {
                "embeddings": [
                    [
                        0.1,
                        0.2,
                        0.3,
                    ]
                ]
            }

    client = OllamaClient(
        EmbedTransport()
    )

    result = client.embed(
        "hello"
    )

    assert result == [
        0.1,
        0.2,
        0.3,
    ]
