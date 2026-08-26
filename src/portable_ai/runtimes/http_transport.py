from typing import Any


class HttpTransport:
    """
    HTTP communication boundary.
    """

    def get(
        self,
        url: str,
    ) -> dict[str, Any]:
        raise NotImplementedError
