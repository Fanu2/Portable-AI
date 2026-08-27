from abc import (
    ABC,
    abstractmethod,
)


class AssistantProvider(ABC):
    """
    Assistant generation provider contract.

    Implementations may connect to:
        - local models
        - external APIs
        - future providers

    This boundary hides provider details
    from assistant services.
    """

    @abstractmethod
    def generate(
        self,
        context,
    ):
        """
        Generate assistant response.

        Provider implementations must
        implement this method.
        """

        raise NotImplementedError
