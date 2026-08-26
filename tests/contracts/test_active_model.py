from portable_ai.contracts.active_model import (
    ActiveModel,
)


def test_active_model_stores_selection():

    active = ActiveModel(
        model_name="Qwen3.5-4B",
        runtime_name="ollama",
        capability="text_generation",
    )

    assert (
        active.model_name
        == "Qwen3.5-4B"
    )

    assert (
        active.runtime_name
        == "ollama"
    )

    assert (
        active.capability
        == "text_generation"
    )
