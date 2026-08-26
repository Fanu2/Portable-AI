from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.contracts.execution_result import (
    ExecutionResult,
)


def test_execution_request_contract():

    request = ExecutionRequest(
        runtime="Ollama",
        model="Qwen3.5-4B",
        prompt="Hello",
    )

    assert request.runtime == "Ollama"
    assert request.model == "Qwen3.5-4B"
    assert request.prompt == "Hello"


def test_execution_result_contract():

    result = ExecutionResult(
        runtime="Ollama",
        model="Qwen3.5-4B",
        response="Hello",
    )

    assert result.response == "Hello"
