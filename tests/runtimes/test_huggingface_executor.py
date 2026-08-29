from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.runtimes.huggingface_executor import (
    HuggingFaceExecutor,
)


class FakeProvider:

    def generate(
        self,
        prompt,
        **kwargs,
    ) -> str:

        return "generated response"


def test_execute_returns_execution_result():

    executor = HuggingFaceExecutor(
        FakeProvider()
    )

    request = ExecutionRequest(
        runtime="huggingface",
        model="test-model",
        prompt="Hello",
    )

    result = executor.execute(
        request
    )

    assert result.runtime == "huggingface"

    assert result.model == "test-model"

    assert result.response == "generated response"
