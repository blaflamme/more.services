import morepath
from webtest import TestApp as Client

from .fixtures.app import App


def setup_module(module):
    morepath.disable_implicit()


def test_app():
    c = Client(App())
    response = c.get('/')
    assert response.body == b'The root: ROOT'
