from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)


class ModelQueryService:
    """
    Provides read-only access to registered models.
    """

    def __init__(
        self,
        registry: ModelRegistry,
    ) -> None:

        self._registry = registry

    def all_models(
        self,
    ) -> list[ModelDescriptor]:

        return self._registry.all()
