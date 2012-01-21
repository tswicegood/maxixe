from types import ModuleType


class Scenario(object):
    def __init__(self, name, feature=None):
        self.name = name
        self.steps = (1, 2, 3, )
        self.feature = feature


class FeatureType(ModuleType):
    def __init__(self, name, description, scenarios):
        self.name = name
        self.description = description
        self.scenarios = scenarios
