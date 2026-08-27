from portable_ai.services.active_execution_service import (
    ActiveExecutionService,
)


class FakeRequestService:

    def create_request(
        self,
        prompt,
    ):

        return prompt


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


def test_active_execution_executes():

    adapter = FakeAdapterService()

    service = ActiveExecutionService(
        FakeRequestService(),
        adapter,
    )

    result = service.execute(
        "Hello"
    )

    assert result == "ok"

    assert (
        adapter.received
        == "Hello"
    )
