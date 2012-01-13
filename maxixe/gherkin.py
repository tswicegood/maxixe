from types import ModuleType


class Scenario(object):
    def __init__(self):
        self.name = "Found feature"
        self.steps = (1, 2, 3, )


class FeatureType(ModuleType):
    def __init__(self, name, description, scenarios):
        self.name = name
        self.description = description
        self.scenarios = scenarios