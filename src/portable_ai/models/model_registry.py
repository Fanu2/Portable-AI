from portable_ai.contracts.model_descriptor import ModelDescriptor


class ModelRegistry:
    """
    Registry of available local AI models.
    """

    def __init__(self) -> None:
        self._models: dict[str, ModelDescriptor] = {}

    def register(self, model: ModelDescriptor) -> None:
        self._models[model.name] = model

    def get(self, name: str) -> ModelDescriptor | None:
        return self._models.get(name)

    def all(self) -> list[ModelDescriptor]:
        return list(self._models.values())

    def available_for_capability(
        self,
        capability: str,
    ) -> list[ModelDescriptor]:
        return [
            model
            for model in self._models.values()
            if capability in model.capabilities
        ]
