from pathlib import Path

from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_application_factory_exposes_hardware_detection(
    tmp_path,
):

    context = ApplicationFactory(
        Path(tmp_path)
    ).create()

    assert (
        context.hardware_detection
        is not None
    )

    info = (
        context.hardware_detection.detect()
    )

    assert (
        info.cpu_cores >= 1
    )

    assert (
        info.ram_gb >= 0
    )

    assert (
        info.storage_gb >= 0
    )
