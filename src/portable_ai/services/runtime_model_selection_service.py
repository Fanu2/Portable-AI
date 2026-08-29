from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)

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

from portable_ai.services.hardware_model_compatibility_service import (
    HardwareModelCompatibilityService,
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

        self._hardware_compatibility = (
            HardwareModelCompatibilityService()
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

        matching_models = [
            model
            for model in models
            if model.source_runtime == runtime_name
        ]

        generic_models = [
            model
            for model in models
            if model.source_runtime is None
        ]

        for model in (
            matching_models
            + generic_models
        ):

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

    def select_with_hardware(
        self,
        capability: str,
        runtime_name: str,
        hardware: HardwareInfo,
    ):

        models = (
            self._models.available_for_capability(
                capability
            )
        )

        matching_models = [
            model
            for model in models
            if model.source_runtime == runtime_name
        ]

        generic_models = [
            model
            for model in models
            if model.source_runtime is None
        ]

        for model in (
            matching_models
            + generic_models
        ):

            if not self._compatibility.can_execute(
                model.name,
                runtime_name,
            ):
                continue

            if not self._hardware_compatibility.can_run(
                model,
                hardware,
            ):
                continue

            return ModelSelectionResult(
                model=model,
                runtime=runtime_name,
                capability=capability,
                reason=(
                    "matched capability, "
                    "runtime, and hardware"
                ),
            )

        return None
