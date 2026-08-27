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

    Confirms contract implementation.
    """

    def retrieve(
        self,
        query: str,
    ):

        return [
            RetrievalResult(
                content="result",
                metadata={
                    "source": "test",
                },
            )
        ]


def test_retrieval_provider_contract():

    provider = FakeRetrievalProvider()

    results = provider.retrieve(
        "query"
    )

    assert len(results) == 1

    assert (
        results[0].content
        == "result"
    )


def test_retrieval_result_metadata():

    result = RetrievalResult(
        content="text",
        metadata={
            "source": "document",
        },
    )

    assert (
        result.metadata["source"]
        == "document"
    )


def test_retrieval_result_is_immutable():

    result = RetrievalResult(
        content="text"
    )

    try:

        result.content = "changed"

        assert False

    except Exception:

        assert True
