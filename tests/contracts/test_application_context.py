from portable_ai.contracts.application_context import (
    ApplicationContext,
)


def test_application_context_creation():
    context = ApplicationContext(
        configuration=None,
        storage=None,
        hardware=None,
    )

    assert context.configuration is None
    assert context.storage is None
    assert context.hardware is None


def test_application_context_optional_services_default_none():
    context = ApplicationContext(
        configuration=None,
        storage=None,
        hardware=None,
    )

    assert context.runtime is None
    assert context.dashboard is None
