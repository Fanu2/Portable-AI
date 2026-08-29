from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.services.model_query_service import (
    ModelQueryService,
)


def test_model_query_service_returns_registered_models():

    registry = ModelRegistry()

    model = ModelDescriptor(
        name="qwen3:4b",
        version="runtime",
        format="GGUF",
        quantization=None,
        size_gb=0.0,
        license="unknown",
        capabilities=frozenset(),
    )

    registry.register(
        model
    )

    service = ModelQueryService(
        registry
    )

    models = service.all_models()

    assert models == [
        model
    ]
