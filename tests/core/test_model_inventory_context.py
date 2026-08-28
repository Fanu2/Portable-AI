from pathlib import Path

from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_application_context_exposes_model_inventory(
    tmp_path,
):

    context = ApplicationFactory(
        Path(tmp_path)
    ).create()

    assert (
        context.model_inventory
        is not None
    )

    models = (
        context.model_inventory.all()
    )

    assert len(models) >= 1

    names = [
        model.model_name
        for model in models
    ]

    assert (
        "qwen3:4b"
        in names
    )
