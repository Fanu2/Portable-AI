from portable_ai.contracts.model_descriptor import ModelDescriptor
from portable_ai.models.catalog.model_catalog import MODEL_DEFINITIONS
from portable_ai.models.model_registry import ModelRegistry


class ModelCatalogService:
    """
    Loads model definitions into the model registry.
    """

    def __init__(
        self,
        registry: ModelRegistry,
    ) -> None:
        self._registry = registry

    def load_catalog(self) -> list[ModelDescriptor]:
        models: list[ModelDescriptor] = []

        for definition in MODEL_DEFINITIONS:
            model = ModelDescriptor(
                name=definition.name,
                version="catalog",
                format=definition.format,
                quantization=definition.default_quantization,
                size_gb=0.0,
                license=definition.license or "unknown",
                capabilities=definition.capabilities,
            )

            self._registry.register(model)
            models.append(model)

        return models
