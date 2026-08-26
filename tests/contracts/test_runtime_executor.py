from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.services.fake_runtime_executor import (
    FakeRuntimeExecutor,
)


def test_runtime_executor_contract():

    executor = FakeRuntimeExecutor()

    result = executor.execute(
        ExecutionRequest(
            runtime="Ollama",
            model="Qwen3.5-4B",
            prompt="Hello",
        )
    )

    assert (
        result.runtime
        == "Ollama"
    )

    assert (
        result.model
        == "Qwen3.5-4B"
    )

    assert (
        result.response
        == "fake response"
    )
