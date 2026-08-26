from portable_ai.contracts.model_resource import (
    ModelResource,
)

from portable_ai.services.model_inventory_service import (
    ModelInventoryService,
)


def test_model_inventory_registers_model():

    service = ModelInventoryService()

    resource = ModelResource(
        model_name="Qwen3.5-4B",
        path="/models/qwen.gguf",
        size_gb=2.7,
        format="GGUF",
    )

    service.register(
        resource
    )

    result = service.get(
        "Qwen3.5-4B"
    )

    assert result is not None

    assert (
        result.model_name
        == "Qwen3.5-4B"
    )


def test_model_inventory_lists_available_models():

    service = ModelInventoryService()

    service.register(
        ModelResource(
            model_name="Qwen3.5-4B",
            path="/models/qwen.gguf",
            size_gb=2.7,
            format="GGUF",
        )
    )

    models = service.available()

    assert len(models) == 1
