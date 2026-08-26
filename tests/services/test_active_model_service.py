from portable_ai.contracts.active_model import (
    ActiveModel,
)

from portable_ai.services.active_model_service import (
    ActiveModelService,
)


class FakeConfigurationService:
    """
    Minimal configuration storage
    used to verify persistence behavior.
    """

    def __init__(
        self,
    ) -> None:

        self._data = {}

    def set(
        self,
        key,
        value,
    ) -> None:

        self._data[key] = value

    def get(
        self,
        key,
    ):

        return self._data.get(
            key
        )


def test_active_model_service_sets_model():
    """
    Verify that ActiveModelService
    stores the selected model state.
    """

    service = ActiveModelService()

    model = ActiveModel(
        model_name="Qwen3.5-4B",
        runtime_name="ollama",
        capability="text_generation",
    )

    service.set_active_model(
        model
    )

    result = (
        service.get_active_model()
    )

    assert result is not None

    assert (
        result.model_name
        == "Qwen3.5-4B"
    )

    assert (
        result.runtime_name
        == "ollama"
    )


def test_active_model_service_clears_model():
    """
    Verify that active model state
    can be removed.
    """

    service = ActiveModelService()

    service.set_active_model(
        ActiveModel(
            model_name="Qwen3.5-4B",
            runtime_name="ollama",
        )
    )

    service.clear_active_model()

    assert (
        service.get_active_model()
        is None
    )


def test_active_model_service_restores_model():
    """
    Verify that active model selection
    survives service recreation.

    Persistence flow:

        ActiveModelService
                |
                ▼
        ConfigurationService
                |
                ▼
        Restore previous selection
    """

    configuration = (
        FakeConfigurationService()
    )

    service = ActiveModelService(
        configuration
    )

    service.set_active_model(
        ActiveModel(
            model_name="Qwen3.5-4B",
            runtime_name="ollama",
            capability="text_generation",
        )
    )

    # Simulate application restart
    restored_service = ActiveModelService(
        configuration
    )

    restored_service.restore()

    result = (
        restored_service.get_active_model()
    )

    assert result is not None

    assert (
        result.model_name
        == "Qwen3.5-4B"
    )

    assert (
        result.runtime_name
        == "ollama"
    )

    assert (
        result.capability
        == "text_generation"
    )
