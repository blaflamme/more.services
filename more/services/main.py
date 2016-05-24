from dectate import Action
from morepath import App
from morepath.directive import SettingAction
from morepath.settings import SettingRegistry
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

    factory_arguments = {
        'setting_registry': SettingRegistry
        }

    def __init__(self, setting_registry):
        self._setting_registry = setting_registry
        super().__init__()

    def register_service(self, obj, name):
        self.register_predicates(
            name,
            [match_argname('obj')]
        )
        self.register_value(
            name,
            [Service],
            obj(self, self._setting_registry)
        )

    def find(self, name):
        return self.component(name, Service)


@ServiceApp.directive('service')
class ServiceAction(Action):
    depends = [SettingAction]

    config = {
        'service_registry': ServiceRegistry
    }

    def __init__(self, name):
        self.name = name

    def identifier(self, service_registry):
        return ('service', self.name)

    def perform(self, obj, service_registry):
        service_registry.register_service(obj, self.name)
