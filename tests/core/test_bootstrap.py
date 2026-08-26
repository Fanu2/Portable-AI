from portable_ai.contracts.application_context import (
    ApplicationContext,
)
from portable_ai.core.bootstrap import ApplicationBootstrap


def test_application_bootstrap_returns_context():
    context = ApplicationContext(
        configuration=None,
        storage=None,
        hardware=None,
    )

    bootstrap = ApplicationBootstrap(
        context
    )

    assert bootstrap.build() == context
