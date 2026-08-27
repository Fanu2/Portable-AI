from abc import ABC, abstractmethod


class RetrievalProvider(ABC):
    """
    Retrieval provider contract.

    Implementations may connect to:
        - local indexes
        - vector stores
        - future search systems

    Does not:
        - manage documents
        - create indexes
        - store data
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
    ):
        """
        Retrieve relevant context.

        Returns provider-defined results.
        """

        raise NotImplementedError
