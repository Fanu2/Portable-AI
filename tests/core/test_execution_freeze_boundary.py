from pathlib import Path

from portable_ai.contracts.execution_request import (
    ExecutionRequest,
)

from portable_ai.core.application_factory import (
    ApplicationFactory,
)


def test_execution_foundation_freeze_boundary(
    tmp_path,
):

    context = ApplicationFactory(
        Path(tmp_path)
    ).create()

    assert (
        context.execution
        is not None
    )

    result = context.execution.execute(
        "ollama",
        ExecutionRequest(
            runtime="ollama",
            model="Qwen3.5-4B",
            prompt="hello",
        ),
    )

    # Runtime may be unavailable in CI,
    # but execution boundary must remain safe.
    assert (
        result is None
        or result.response is not None
    )
