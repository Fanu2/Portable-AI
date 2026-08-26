from portable_ai.models.executor_registry import (
    ExecutorRegistry,
)

from portable_ai.services.fake_runtime_executor import (
    FakeRuntimeExecutor,
)


def test_executor_registry_registers_executor():

    registry = ExecutorRegistry()

    executor = FakeRuntimeExecutor()

    registry.register(
        "ollama",
        executor,
    )

    assert (
        registry.get("ollama")
        == executor
    )


def test_executor_registry_lists_names():

    registry = ExecutorRegistry()

    registry.register(
        "ollama",
        FakeRuntimeExecutor(),
    )

    assert (
        "ollama"
        in registry.all_names()
    )
