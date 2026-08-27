from portable_ai.assistant.response_generation_service import (
    ResponseGenerationService,
)

from portable_ai.assistant.providers.assistant_provider import (
    AssistantProvider,
)


class FakeExecutor(
    AssistantProvider
):
    """
    Fake assistant provider.

    Matches AssistantProvider contract.
    """

    def generate(
        self,
        context,
    ):

        return "generated response"


def test_response_generation_boundary():

    service = ResponseGenerationService(
        FakeExecutor()
    )

    result = service.generate(
        "context"
    )

    assert (
        result
        == "generated response"
    )
