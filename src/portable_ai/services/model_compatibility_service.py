from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)

from portable_ai.contracts.model_resource import (
    ModelResource,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.services.hardware_model_compatibility_service import (
    HardwareModelCompatibilityService,
)


class ModelCompatibilityService:
    """
    Provides model capability and hardware matching.
    """

    def __init__(
        self,
        registry: ModelRegistry,
        hardware_service: HardwareModelCompatibilityService | None = None,
    ) -> None:

        self._registry = registry

        self._hardware_service = (
            hardware_service
        )

    def supports(
        self,
        model_name: str,
        capability: str,
    ) -> bool:

        model = self._registry.get(
            model_name
        )

        if model is None:

            return False

        return (
            capability
            in model.capabilities
        )

    def available_for_capability(
        self,
        capability: str,
    ):

        return (
            self._registry
            .available_for_capability(
                capability
            )
        )

    def can_run(
        self,
        model: ModelResource,
        hardware: HardwareInfo,
    ) -> bool:

        if self._hardware_service is None:

            return True

        return (
            self._hardware_service.can_run(
                model,
                hardware,
            )
        )
