from portable_ai.models.model_registry import (
    ModelRegistry,
)


class ModelSelectionService:
    """
    Selects models based on capability.
    """

    def __init__(
        self,
        registry: ModelRegistry,
    ) -> None:
        self._registry = registry

    def select_for_capability(
        self,
        capability: str,
    ):
        models = (
            self._registry.available_for_capability(
                capability
            )
        )

        if not models:
            return None

        return models[0]
