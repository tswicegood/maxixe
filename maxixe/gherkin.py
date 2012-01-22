from types import ModuleType

from . import utils


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
        return all([a.runnable for a in self.steps])


class FeatureType(ModuleType):
    def __init__(self, name, description):
        if not hasattr(self, "__path__"):
            self.__path__ = []
        self.name = name
        self.description = description
        self.scenarios = []
