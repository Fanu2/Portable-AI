from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.models.executor_registry import (
    ExecutorRegistry,
)

from portable_ai.services.execution_service import (
    ExecutionService,
)

from portable_ai.services.fake_runtime_executor import (
    FakeRuntimeExecutor,
)

from portable_ai.services.execution_result_validator import (
    ExecutionResultValidator,
)


def test_execution_service_executes_request():

    registry = ExecutorRegistry()

    registry.register(
        "ollama",
        FakeRuntimeExecutor(),
    )

    service = ExecutionService(
        registry,
        ExecutionResultValidator(),
    )

    result = service.execute(
        "ollama",
        ExecutionRequest(
            runtime="Ollama",
            model="Qwen3.5-4B",
            prompt="Hello",
        ),
    )

    assert result is not None

    assert (
        result.response
        == "fake response"
    )


def test_execution_service_returns_none_for_unknown_executor():

    registry = ExecutorRegistry()

    service = ExecutionService(
        registry,
        ExecutionResultValidator(),
    )

    result = service.execute(
        "missing",
        ExecutionRequest(
            runtime="Ollama",
            model="Qwen3.5-4B",
            prompt="Hello",
        ),
    )

    assert result is None
