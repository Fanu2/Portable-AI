from pathlib import Path

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


def test_model_inventory_scans_installed_models(
    tmp_path: Path,
):

    model_file = (
        tmp_path / "qwen-local.gguf"
    )

    model_file.write_bytes(
        b"model-data"
    )

    service = ModelInventoryService()

    service.scan(
        [
            tmp_path,
        ]
    )

    models = service.installed()

    assert len(models) == 1

    assert (
        models[0].model_name
        == "qwen-local"
    )

    assert (
        models[0].format
        == "GGUF"
    )

    assert (
        models[0].installed
        is True
    )
