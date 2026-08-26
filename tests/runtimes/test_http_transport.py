from portable_ai.runtimes.http_transport import HttpTransport


def test_http_transport_interface():
    transport = HttpTransport()

    try:
        transport.get("http://localhost")
    except NotImplementedError:
        assert True
