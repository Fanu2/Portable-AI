from pathlib import Path

from portable_ai.core.application_factory import (
    ApplicationFactory,
)

from portable_ai.runtimes.ollama_executor import (
    OllamaExecutor,
)


def test_application_factory_creates_context(tmp_path):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    assert context.configuration is not None
    assert context.runtime is not None
    assert context.dashboard is not None
    assert context.monitor is not None
    assert context.capabilities is not None
    assert context.model_catalog is not None
    assert context.model_selection is not None
    assert context.execution is not None


def test_application_factory_registers_ollama(tmp_path):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    runtimes = (
        context.runtime._registry.all_named()
    )

    assert "ollama" in runtimes


def test_application_factory_exposes_monitor(tmp_path):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    snapshot = context.monitor.check(
        "ollama"
    )

    assert (
        snapshot.runtime_name
        == "ollama"
    )

    assert snapshot.health is not None

    assert snapshot.checked_at is not None


def test_application_factory_exposes_capabilities(
    tmp_path,
):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    capabilities = (
        context.capabilities.for_runtime(
            "ollama"
        )
    )

    names = [
        capability.name
        for capability in capabilities
    ]

    assert (
        "ollama:text_generation"
        in names
    )


def test_application_factory_loads_model_catalog(
    tmp_path,
):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    model = (
        context.model_selection.select(
            "text_generation",
            "Ollama",
        )
    )

    assert model is not None

    assert (
        model.model.name
        == "Qwen3.5-4B"
    )

    assert (
        model.runtime
        == "Ollama"
    )

    assert (
        model.capability
        == "text_generation"
    )


def test_application_factory_exposes_execution(
    tmp_path,
):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    assert (
        context.execution
        is not None
    )


def test_application_factory_registers_real_ollama_executor(
    tmp_path,
):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    executor = (
        context.execution
        ._registry
        .get("ollama")
    )

    assert executor is not None

    assert isinstance(
        executor,
        OllamaExecutor,
    )

def test_application_factory_uses_configured_assistant_model(
    tmp_path,
):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    ollama = (
        context.runtime
        ._registry
        .get("ollama")
    )

    assert ollama is not None

    assert (
        ollama._client._model
        == "qwen3:4b"
    )
def test_application_factory_exposes_runtime_sync(
    tmp_path,
):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    assert (
        context.runtime_sync
        is not None
    )

def test_application_factory_exposes_portable_storage(
    tmp_path,
):

    factory = ApplicationFactory(
        Path(tmp_path)
    )

    context = factory.create()

    assert context.storage is not None

    assert context.storage.root() == Path(
        tmp_path
    )

    assert context.storage.models().exists()
    assert context.storage.data().exists()
    assert context.storage.config().exists()
