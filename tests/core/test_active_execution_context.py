from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_application_context_exposes_active_execution(
    tmp_path,
):

    context = ApplicationFactory(
        tmp_path
    ).create()

    assert (
        context.active_execution
        is not None
    )
