from portable_ai.contracts.execution_result import (
    ExecutionResult,
)

from portable_ai.services.execution_result_validator import (
    ExecutionResultValidator,
)


def test_execution_result_validator_accepts_valid_result():

    validator = ExecutionResultValidator()

    result = ExecutionResult(
        runtime="ollama",
        model="Qwen3.5-4B",
        response="hello",
    )

    assert validator.validate(
        result
    )


def test_execution_result_validator_rejects_empty_response():

    validator = ExecutionResultValidator()

    result = ExecutionResult(
        runtime="ollama",
        model="Qwen3.5-4B",
        response="",
    )

    assert not validator.validate(
        result
    )
