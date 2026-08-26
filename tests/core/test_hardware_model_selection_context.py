from pathlib import Path

from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)

from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_application_context_supports_hardware_aware_selection(
    tmp_path,
):

    context = ApplicationFactory(
        Path(tmp_path)
    ).create()

    assert (
        context.model_selection
        is not None
    )

    assert (
        context.hardware_detection
        is not None
    )

    hardware = (
        context.hardware_detection.detect()
    )

    result = (
        context.model_selection.select_with_hardware(
            "text_generation",
            "Ollama",
            hardware,
        )
    )

    assert result is not None

    assert (
        result.model.name
        == "Qwen3.5-4B"
    )
