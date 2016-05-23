from dectate import Action
from morepath import App
from reg import (
    Registry,
    match_argname
    )


class Service(object):
    pass


class ServiceApp(App):

    def find_service(self, name):
        return self.config.service_registry.find(name)


class ServiceRegistry(Registry):

    def find(self, name):
        return self.component(name, Service)


@ServiceApp.directive('service')
class ServiceAction(Action):
    config = {
        'service_registry': ServiceRegistry
    }

    def __init__(self, name):
        self.name = name

    def identifier(self, service_registry):
        return ('service', self.name)

    def perform(self, obj, service_registry):
        service_registry.register_predicates(
            self.name,
            [match_argname('obj')]
        )
        service_registry.register_value(
            self.name,
            [Service],
            obj(service_registry)
        )
