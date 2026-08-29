from portable_ai.runtimes.huggingface_client import (
    HuggingFaceClient,
)


class FakeGenerator:

    def __call__(
        self,
        prompt,
        **kwargs,
    ):

        return [
            {
                "generated_text":
                    prompt + " test response"
            }
        ]


def test_model_returns_configured_model():

    client = HuggingFaceClient(
        model="test-model",
    )

    assert client.model() == "test-model"


def test_generate_uses_loaded_generator():

    client = HuggingFaceClient()

    client._generator = FakeGenerator()

    result = client.generate(
        "Hello",
        max_new_tokens=5,
    )

    assert result == "Hello test response"
