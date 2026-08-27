from portable_ai.runtimes.http_transport import (
    HttpTransport,
)


def test_http_transport_interface():

    transport = HttpTransport()

    assert hasattr(
        transport,
        "get",
    )

    assert hasattr(
        transport,
        "post",
    )
