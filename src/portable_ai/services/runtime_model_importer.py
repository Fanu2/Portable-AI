from portable_ai.contracts.model_descriptor import ModelDescriptor
from portable_ai.models.model_registry import ModelRegistry


class RuntimeModelImporter:
    """
    Imports runtime models into Portable-AI registry.
    """

    def __init__(
        self,
        registry: ModelRegistry,
    ) -> None:
        self._registry = registry

    def import_models(
        self,
        runtime_name: str,
        model_names: list[str],
    ) -> list[ModelDescriptor]:
        models: list[ModelDescriptor] = []

        for name in model_names:
            model = ModelDescriptor(
                name=name,
                version="runtime",
                format="unknown",
                quantization=None,
                size_gb=0.0,
                license="unknown",
                capabilities=frozenset(),
                source_runtime=runtime_name,
            )

            self._registry.register(model)
            models.append(model)

        return models
