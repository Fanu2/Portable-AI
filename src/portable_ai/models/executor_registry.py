from portable_ai.contracts.runtime_executor import (
    RuntimeExecutor,
)


class ExecutorRegistry:
    """
    Registry of runtime executors.
    """

    def __init__(self) -> None:
        self._executors: dict[
            str,
            RuntimeExecutor,
        ] = {}

    def register(
        self,
        name: str,
        executor: RuntimeExecutor,
    ) -> None:
        self._executors[name] = executor

    def get(
        self,
        name: str,
    ) -> RuntimeExecutor | None:
        return self._executors.get(
            name
        )

    def all_names(self) -> list[str]:
        return list(
            self._executors.keys()
        )
