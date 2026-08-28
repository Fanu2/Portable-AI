from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)


class RuntimeModelImporter:
    """
    Imports runtime models into the Portable-AI registry.

    Existing catalog metadata is preserved when a
    discovered runtime model already exists in the
    registry.

    Runtime provenance is added through
    ``source_runtime``.
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

            existing = (
                self._registry.get(
                    name
                )
            )

            if existing is not None:

                model = ModelDescriptor(
                    name=existing.name,
                    version=existing.version,
                    format=existing.format,
                    quantization=(
                        existing.quantization
                    ),
                    size_gb=existing.size_gb,
                    license=existing.license,
                    capabilities=(
                        existing.capabilities
                    ),
                    minimum_ram_gb=(
                        existing.minimum_ram_gb
                    ),
                    checksum=existing.checksum,
                    source_runtime=runtime_name,
                )

            else:

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

            self._registry.register(
                model
            )

            models.append(
                model
            )

        return models
