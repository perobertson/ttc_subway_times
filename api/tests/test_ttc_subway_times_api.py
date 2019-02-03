from ttc_subway_times_api import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_hello(client):
    rv = client.get('/hello')
    assert b'Hello, World!' == rv.data
