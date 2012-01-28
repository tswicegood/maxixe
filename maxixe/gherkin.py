from types import ModuleType

from . import utils


# TODO: add property for getting at function
# TODO: add run function for executing
class Step(object):
    def __init__(self, description, scenario):
        self.description = description
        self.scenario = scenario

    @property
    def has_run(self):
        return False

    @property
    def runnable(self):
        return utils.has_matching_step(self)


class Scenario(object):
    def __init__(self, name, feature):
        self.name = name
        self.steps = []
        self.feature = feature

    @property
    def runnable(self):
        return self.steps[0].runnable


class FeatureType(ModuleType):
    def __init__(self, name, description):
        if not hasattr(self, "__path__"):
            self.__path__ = []
        self.name = name
        self.description = description
        self.scenarios = []
