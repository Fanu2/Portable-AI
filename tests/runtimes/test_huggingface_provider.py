from portable_ai.runtimes.huggingface_provider import (
    HuggingFaceRuntimeProvider,
)


class FakeClient:

    def __init__(
        self,
    ) -> None:

        self.loaded = False

    def model(
        self,
    ) -> str:

        return "test-model"

    def load(
        self,
    ) -> None:

        self.loaded = True

    def generate(
        self,
        prompt,
        **kwargs,
    ) -> str:

        return "generated response"

    def health(
        self,
    ) -> bool:

        return True


def test_discover_returns_model():

    provider = HuggingFaceRuntimeProvider(
        FakeClient()
    )

    result = provider.discover()

    assert result == {
        "models": [
            "test-model",
        ],
    }


def test_capabilities():

    provider = HuggingFaceRuntimeProvider(
        FakeClient()
    )

    assert provider.capabilities() == {
        "text_generation",
    }


def test_load_model_loads_client():

    client = FakeClient()

    provider = HuggingFaceRuntimeProvider(
        client
    )

    assert provider.load_model(
        "test-model"
    ) is True

    assert client.loaded is True


def test_generate_delegates_to_client():

    provider = HuggingFaceRuntimeProvider(
        FakeClient()
    )

    result = provider.generate(
        "Hello"
    )

    assert result == "generated response"


def test_health_delegates_to_client():

    provider = HuggingFaceRuntimeProvider(
        FakeClient()
    )

    assert provider.health() is True
