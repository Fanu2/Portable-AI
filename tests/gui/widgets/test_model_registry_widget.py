from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.services.model_query_service import (
    ModelQueryService,
)

from portable_ai.gui.widgets.model_registry_widget import (
    ModelRegistryWidget,
)


def test_model_registry_widget_displays_models(
    qtbot,
):

    registry = ModelRegistry()

    registry.register(
        ModelDescriptor(
            name="qwen3:4b",
            version="runtime",
            format="GGUF",
            quantization=None,
            size_gb=2.7,
            license="unknown",
            capabilities=frozenset(
                {
                    "text_generation",
                }
            ),
            source_runtime="ollama",
        )
    )

    service = ModelQueryService(
        registry
    )

    widget = ModelRegistryWidget(
        service
    )

    qtbot.addWidget(
        widget
    )

    assert (
        "qwen3:4b"
        in widget._label.text()
    )

    assert (
        "ollama"
        in widget._label.text()
    )
