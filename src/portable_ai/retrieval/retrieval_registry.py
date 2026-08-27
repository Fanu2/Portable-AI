class RetrievalRegistry:
    """
    Stores retrieval providers.

    Responsibilities:
        - register retrieval providers
        - retrieve providers
        - isolate provider lookup

    Does not:
        - execute retrieval
        - select algorithms
        - manage indexes
    """

    def __init__(
        self,
    ) -> None:

        self._providers = {}

    def register(
        self,
        name: str,
        provider,
    ) -> None:
        """
        Register retrieval provider.
        """

        self._providers[name] = provider

    def get(
        self,
        name: str,
    ):
        """
        Retrieve provider.
        """

        return self._providers.get(
            name
        )

    def names(
        self,
    ) -> list[str]:
        """
        Return registered provider names.
        """

        return list(
            self._providers.keys()
        )
