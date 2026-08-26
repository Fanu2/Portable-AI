from portable_ai.models.executor_registry import (
    ExecutorRegistry,
)

from portable_ai.runtimes.ollama_executor import (
    OllamaExecutor,
)


def test_executor_registry_freeze_boundary():

    registry = ExecutorRegistry()

    executor = OllamaExecutor(
        None,
    )

    registry.register(
        "ollama",
        executor,
    )

    assert (
        registry.get("ollama")
        == executor
    )
