from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)


def test_execution_request_stores_request():

    request = ExecutionRequest(
        model_name="Qwen3.5-4B",
        runtime_name="ollama",
        prompt="Explain local AI",
        capability="text_generation",
    )

    assert (
        request.model_name
        == "Qwen3.5-4B"
    )

    assert (
        request.runtime_name
        == "ollama"
    )

    assert (
        request.prompt
        == "Explain local AI"
    )

    assert (
        request.capability
        == "text_generation"
    )
