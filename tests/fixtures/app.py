from more.services import ServiceApp


class App(ServiceApp):
    pass


@App.service(name='test')
def test_service(registry, settings):
    return 'SERVICE'


@App.path(path='/')
class Root(object):
    def __init__(self, request):
        value = request.app.find_service('test')
        self.value = value


@App.view(model=Root)
def root_default(self, request):
    return "The root: %s" % self.value
