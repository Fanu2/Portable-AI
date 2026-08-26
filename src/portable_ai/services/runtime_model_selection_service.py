from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.models.runtime_registry import (
    RuntimeRegistry,
)

from portable_ai.models.model_selection_result import (
    ModelSelectionResult,
)

from portable_ai.services.runtime_model_compatibility_service import (
    RuntimeModelCompatibilityService,
)


class RuntimeModelSelectionService:
    """
    Selects a model and runtime combination.
    """

    def __init__(
        self,
        model_registry: ModelRegistry,
        runtime_registry: RuntimeRegistry,
    ) -> None:

        self._models = model_registry

        self._compatibility = (
            RuntimeModelCompatibilityService(
                model_registry,
                runtime_registry,
            )
        )

    def select(
        self,
        capability: str,
        runtime_name: str,
    ):

        models = (
            self._models.available_for_capability(
                capability
            )
        )

        for model in models:

            if self._compatibility.can_execute(
                model.name,
                runtime_name,
            ):

                return ModelSelectionResult(
                    model=model,
                    runtime=runtime_name,
                    capability=capability,
                    reason=(
                        "matched capability "
                        "and runtime"
                    ),
                )

        return None
