from pathlib import Path

from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_capability_foundation_freeze_boundary(
    tmp_path,
):
    context = ApplicationFactory(
        Path(tmp_path)
    ).create()

    assert (
        context.capabilities
        is not None
    )

    capabilities = (
        context.capabilities.for_runtime(
            "ollama"
        )
    )

    names = [
        capability.name
        for capability in capabilities
    ]

    assert (
        "ollama:text_generation"
        in names
    )

    assert (
        "ollama:embeddings"
        in names
    )
