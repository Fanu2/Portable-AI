from portable_ai.services.retrieval_service import (
    RetrievalService,
)

from portable_ai.retrieval.retrieval_contract import (
    RetrievalProvider,
)

from portable_ai.retrieval.retrieval_result import (
    RetrievalResult,
)


class FakeRetrievalProvider(
    RetrievalProvider
):
    """
    Fake retrieval provider.
    """

    def retrieve(
        self,
        query: str,
    ):

        return [
            RetrievalResult(
                content="sample result"
            )
        ]


def test_retrieval_service_delegates_to_provider():

    service = RetrievalService(
        FakeRetrievalProvider()
    )

    results = service.retrieve(
        "hello"
    )

    assert len(results) == 1

    assert (
        results[0].content
        == "sample result"
    )


def test_retrieval_service_without_provider_returns_empty():

    service = RetrievalService()

    results = service.retrieve(
        "hello"
    )

    assert results == []
