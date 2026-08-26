from portable_ai.contracts.model_resource import (
    ModelResource,
)


class ModelInventoryService:
    """
    Tracks available local model resources.
    """

    def __init__(
        self,
    ) -> None:

        self._models: dict[
            str,
            ModelResource,
        ] = {}

    def register(
        self,
        resource: ModelResource,
    ) -> None:

        self._models[
            resource.model_name
        ] = resource

    def get(
        self,
        model_name: str,
    ) -> ModelResource | None:

        return self._models.get(
            model_name
        )

    def all(
        self,
    ) -> list[ModelResource]:

        return list(
            self._models.values()
        )

    def available(
        self,
    ) -> list[ModelResource]:

        return [
            resource
            for resource in self._models.values()
            if resource.available
        ]
