from portable_ai.models.runtime_registry import (
    RuntimeRegistry,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)


class RuntimeModelCompatibilityService:
    """
    Matches models with compatible runtimes.
    """

    def __init__(
        self,
        model_registry: ModelRegistry,
        runtime_registry: RuntimeRegistry,
    ) -> None:
        self._models = model_registry
        self._runtimes = runtime_registry

    def can_execute(
        self,
        model_name: str,
        runtime_name: str,
    ) -> bool:

        model = self._models.get(
            model_name
        )

        runtime = self._runtimes.get(
            runtime_name
        )

        if model is None or runtime is None:
            return False

        capabilities = runtime.capabilities

        if callable(capabilities):
            runtime_capabilities = capabilities()
        else:
            runtime_capabilities = capabilities

        return model.capabilities.issubset(
            runtime_capabilities
        )
