from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ModelRegistryWidget(QWidget):
    """
    Displays registered Portable-AI models.

    Includes catalog models and models
    discovered from configured runtimes.
    """

    def __init__(
        self,
        model_query_service,
    ) -> None:

        super().__init__()

        self._service = model_query_service

        self._label = QLabel()

        layout = QVBoxLayout()

        layout.addWidget(
            self._label
        )

        self.setLayout(
            layout
        )

        self.refresh()

    def refresh(
        self,
    ) -> None:

        models = (
            self._service.all_models()
        )

        catalog_models = [
            model
            for model in models
            if model.source_runtime is None
        ]

        runtime_models = [
            model
            for model in models
            if model.source_runtime is not None
        ]

        text = (
            "Registered Models\n"
            "=================\n\n"
        )

        if catalog_models:

            text += (
                "CATALOG MODELS\n"
                "--------------\n"
            )

            for model in catalog_models:

                text += (
                    f"{model.name}\n"
                    f"Version: {model.version}\n"
                    f"Format: {model.format}\n"
                    f"Size: {model.size_gb} GB\n"
                )

                if model.quantization:

                    text += (
                        f"Quantization: "
                        f"{model.quantization}\n"
                    )

                if model.capabilities:

                    capabilities = (
                        ", ".join(
                            sorted(
                                model.capabilities
                            )
                        )
                    )

                    text += (
                        f"Capabilities: "
                        f"{capabilities}\n"
                    )

                text += "\n"

        if runtime_models:

            text += (
                "RUNTIME MODELS\n"
                "--------------\n"
            )

            for model in runtime_models:

                text += (
                    f"{model.name}\n"
                    f"Version: {model.version}\n"
                    f"Format: {model.format}\n"
                    f"Size: {model.size_gb} GB\n"
                    f"Runtime: "
                    f"{model.source_runtime}\n"
                )

                if model.quantization:

                    text += (
                        f"Quantization: "
                        f"{model.quantization}\n"
                    )

                if model.capabilities:

                    capabilities = (
                        ", ".join(
                            sorted(
                                model.capabilities
                            )
                        )
                    )

                    text += (
                        f"Capabilities: "
                        f"{capabilities}\n"
                    )

                text += "\n"

        if not models:

            text += (
                "No registered models\n"
            )

        self._label.setText(
            text
        )
