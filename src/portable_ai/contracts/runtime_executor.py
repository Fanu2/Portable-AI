from abc import ABC, abstractmethod

from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.contracts.execution_result import (
    ExecutionResult,
)


class RuntimeExecutor(ABC):
    """
    Defines runtime execution boundary.
    """

    @abstractmethod
    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:
        pass
