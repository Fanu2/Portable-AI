from portable_ai.contracts.active_model import (
    ActiveModel,
)

from portable_ai.services.active_model_service import (
    ActiveModelService,
)

from portable_ai.services.execution_request_service import (
    ExecutionRequestService,
)


def test_execution_request_service_creates_request():

    active_model = ActiveModelService()

    active_model.set_active_model(
        ActiveModel(
            model_name="Qwen3.5-4B",
            runtime_name="ollama",
            capability="text_generation",
        )
    )

    service = ExecutionRequestService(
        active_model
    )

    request = (
        service.create_request(
            "Explain local AI"
        )
    )

    assert request is not None

    assert (
        request.model
        == "Qwen3.5-4B"
    )

    assert (
        request.runtime
        == "ollama"
    )

    assert (
        request.prompt
        == "Explain local AI"
    )


def test_execution_request_service_returns_none_without_model():

    active_model = ActiveModelService()

    service = ExecutionRequestService(
        active_model
    )

    request = (
        service.create_request(
            "Hello"
        )
    )

    assert request is None
