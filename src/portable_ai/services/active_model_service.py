from portable_ai.contracts.active_model import (
    ActiveModel,
)


class ActiveModelService:
    """
    Manages the currently selected model.

    Responsible for:
        - storing active model state
        - restoring saved model state

    Does not execute models.
    """

    def __init__(
        self,
        configuration_service=None,
    ) -> None:

        self._configuration = (
            configuration_service
        )

        self._active_model = None

    def set_active_model(
        self,
        model: ActiveModel,
    ) -> None:

        self._active_model = model

        self._save()

    def get_active_model(
        self,
    ) -> ActiveModel | None:

        return self._active_model

    def clear_active_model(
        self,
    ) -> None:

        self._active_model = None

        self._save()

    def restore(
        self,
    ) -> None:

        if self._configuration is None:

            return

        data = (
            self._configuration.get(
                "active_model"
            )
        )

        if not data:

            return

        self._active_model = ActiveModel(
            model_name=data["model_name"],
            runtime_name=data["runtime_name"],
            capability=data.get(
                "capability"
            ),
        )

    def _save(
        self,
    ) -> None:

        if self._configuration is None:

            return

        if self._active_model is None:

            self._configuration.set(
                "active_model",
                None,
            )

            return

        self._configuration.set(
            "active_model",
            {
                "model_name":
                    self._active_model.model_name,

                "runtime_name":
                    self._active_model.runtime_name,

                "capability":
                    self._active_model.capability,
            },
        )
