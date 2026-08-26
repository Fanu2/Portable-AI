from portable_ai.services.runtime_model_importer import (
    RuntimeModelImporter,
)


class RuntimeSyncService:
    """
    Synchronizes runtime models into Portable-AI.
    """

    def __init__(
        self,
        importer: RuntimeModelImporter,
    ) -> None:
        self._importer = importer

    def sync(
        self,
        runtime_name: str,
        models: list[str],
    ):
        return self._importer.import_models(
            runtime_name,
            models,
        )
