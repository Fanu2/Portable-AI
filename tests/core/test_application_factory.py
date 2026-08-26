from pathlib import Path

from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_application_factory_creates_context(tmp_path):
    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    assert context.configuration is not None
