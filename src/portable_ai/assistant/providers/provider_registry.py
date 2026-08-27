class ProviderRegistry:
    """
    Stores assistant providers.

    Responsibilities:
        - register providers
        - retrieve providers
        - isolate provider lookup

    Does not:
        - execute providers
        - select models
        - manage runtimes
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
        Register provider.
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
        Return registered names.
        """

        return list(
            self._providers.keys()
        )
