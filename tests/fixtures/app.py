from more.services import ServiceApp


class App(ServiceApp):
    pass


@App.path(path='/')
class Root(object):
    def __init__(self):
        self.value = 'ROOT'


@App.view(model=Root)
def root_default(self, request):
    return "The root: %s" % self.value
