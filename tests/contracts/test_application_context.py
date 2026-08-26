from portable_ai.contracts.application_context import ApplicationContext


def test_application_context_creation():
    context = ApplicationContext(
        configuration=None,
        storage=None,
        hardware=None,
    )

    assert context.configuration is None
