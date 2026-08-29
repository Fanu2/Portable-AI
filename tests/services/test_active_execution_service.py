from portable_ai.services.active_execution_service import (
    ActiveExecutionService,
)


class FakeRequest:

    def __init__(
        self,
        runtime,
    ):

        self.runtime = runtime


class FakeRequestService:

    def create_request(
        self,
        prompt,
    ):

        return FakeRequest(
            "ollama"
        )


class FakeAdapterService:

    def __init__(
        self,
    ):

        self.received = None

    def execute(
        self,
        request,
    ):

        self.received = request

        return "ok"


class FakeReadinessService:

    def check(
        self,
        runtime_name,
    ):

        class Readiness:

            ready = True

        return Readiness()


def test_active_execution_executes():

    adapter = FakeAdapterService()

    service = ActiveExecutionService(
        FakeRequestService(),
        adapter,
        FakeReadinessService(),
    )

    result = service.execute(
        "Hello"
    )

    assert result == "ok"

    assert (
        adapter.received
        is not None
    )

class FakeOfflineReadinessService:

    def check(
        self,
        runtime_name,
    ):

        class Readiness:

            ready = False

        return Readiness()


def test_active_execution_does_not_execute_when_runtime_not_ready():

    adapter = FakeAdapterService()

    service = ActiveExecutionService(
        FakeRequestService(),
        adapter,
        FakeOfflineReadinessService(),
    )

    result = service.execute(
        "Hello"
    )

    assert result is None

    assert (
        adapter.received
        is None
    )
