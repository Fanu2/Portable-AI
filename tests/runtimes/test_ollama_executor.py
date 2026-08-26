from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.runtimes.ollama_executor import (
    OllamaExecutor,
)


class FakeProvider:

    def generate(
        self,
        prompt,
        **kwargs,
    ):
        return "generated response"


def test_ollama_executor_executes():

    executor = OllamaExecutor(
        FakeProvider()
    )

    result = executor.execute(
        ExecutionRequest(
            runtime="ollama",
            model="Qwen3.5-4B",
            prompt="Hello",
        )
    )

    assert (
        result.response
        == "generated response"
    )

    assert (
        result.model
        == "Qwen3.5-4B"
    )
