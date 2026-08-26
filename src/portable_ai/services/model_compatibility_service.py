from portable_ai.models.model_registry import (
    ModelRegistry,
)


class ModelCompatibilityService:
    """
    Provides model capability matching.
    """

    def __init__(
        self,
        registry: ModelRegistry,
    ) -> None:
        self._registry = registry

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
            self._registry.available_for_capability(
                capability
            )
        )
