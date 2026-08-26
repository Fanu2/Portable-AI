from pathlib import Path

from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_health_boundary_returns_snapshot(
    tmp_path,
):

    context = ApplicationFactory(
        Path(tmp_path)
    ).create()

    snapshot = context.monitor.check(
        "ollama"
    )

    assert (
        snapshot.runtime_name
        == "ollama"
    )

    assert snapshot.health is not None
    assert snapshot.checked_at is not None
