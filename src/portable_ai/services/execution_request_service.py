from portable_ai.contracts.active_model import (
    ActiveModel,
)

from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)


class ExecutionRequestService:
    """
    Creates execution requests from
    active model state.

    This service connects:
        - model selection
        - execution boundary

    It does not execute models.
    """

    def __init__(
        self,
        active_model_service,
    ) -> None:

        self._active_model = (
            active_model_service
        )

    def create_request(
        self,
        prompt: str,
    ) -> ExecutionRequest | None:
        """
        Creates an execution request
        using the current active model.
        """

        active_model = (
            self._active_model
            .get_active_model()
        )

        if active_model is None:

            return None

        return ExecutionRequest(
            runtime=(
                active_model.runtime_name
            ),
            model=(
                active_model.model_name
            ),
            prompt=prompt,
            capability=(
                active_model.capability
            ),
        )
