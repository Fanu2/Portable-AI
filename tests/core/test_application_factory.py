from pathlib import Path

from portable_ai.core.application_factory import (
    ApplicationFactory,
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
