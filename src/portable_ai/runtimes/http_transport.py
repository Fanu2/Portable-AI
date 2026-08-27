import json
from typing import Any
from urllib.request import (
    Request,
    urlopen,
)


class HttpTransport:
    """
    HTTP communication boundary.
    """

    def get(
        self,
        url: str,
    ) -> dict[str, Any]:

        request = Request(
            url,
            method="GET",
        )

        with urlopen(request) as response:

            return json.loads(
                response.read()
                .decode("utf-8")
            )

    def post(
        self,
        url: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:

        data = json.dumps(
            payload
        ).encode("utf-8")

        request = Request(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
            },
            method="POST",
        )

        with urlopen(request) as response:

            return json.loads(
                response.read()
                .decode("utf-8")
            )
