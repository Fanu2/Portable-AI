from transformers import pipeline


class HuggingFaceClient:
    """
    Client boundary for local Hugging Face
    model execution.
    """

    def __init__(
        self,
        model: str = "sshleifer/tiny-gpt2",
    ) -> None:

        self._model = model

        self._generator = None

    def model(
        self,
    ) -> str:
        return self._model

    def load(
        self,
    ) -> None:

        if self._generator is None:

            self._generator = pipeline(
                "text-generation",
                model=self._model,
            )

    def generate(
        self,
        prompt: str,
        **kwargs,
    ) -> str:

        self.load()

        generation_kwargs = {
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True,
        }

        generation_kwargs.update(
            kwargs
        )

        result = self._generator(
            prompt,
            **generation_kwargs,
        )

        return result[0][
            "generated_text"
        ]

    def health(
        self,
    ) -> bool:

        try:

            self.load()

            return True

        except Exception:

            return False
