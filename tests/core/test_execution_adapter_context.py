from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_application_context_exposes_execution_adapter(
    tmp_path,
):

    context = ApplicationFactory(
        tmp_path
    ).create()

    assert (
        context.execution_adapter
        is not None
    )
