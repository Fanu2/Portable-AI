from portable_ai.retrieval.memory_retrieval_provider import (
    MemoryRetrievalProvider,
)

from portable_ai.retrieval.retrieval_result import (
    RetrievalResult,
)


def test_memory_retrieval_provider_returns_results():

    provider = MemoryRetrievalProvider(
        [
            RetrievalResult(
                content="sample"
            )
        ]
    )

    results = provider.retrieve(
        "query"
    )

    assert len(results) == 1

    assert (
        results[0].content
        == "sample"
    )


def test_memory_retrieval_provider_defaults_empty():

    provider = MemoryRetrievalProvider()

    results = provider.retrieve(
        "query"
    )

    assert results == []
