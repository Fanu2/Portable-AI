from portable_ai.core.application_factory import (
    ApplicationFactory,
)

from pathlib import Path


def test_runtime_foundation_freeze_boundary(
    tmp_path,
):

    context = ApplicationFactory(
        Path(tmp_path)
    ).create()

    assert context.runtime is not None
    assert context.dashboard is not None
    assert context.monitor is not None

    assert (
        "ollama"
        in context.runtime._registry.all_named()
    )
