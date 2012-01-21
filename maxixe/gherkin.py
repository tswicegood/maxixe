from types import ModuleType


class Step(object):
	def __init__(self, description, scenario):
		self.description = description
		self.scenario = scenario


class Scenario(object):
    def __init__(self, name, feature=None):
        self.name = name
        self.steps = []
        self.feature = feature


class FeatureType(ModuleType):
    def __init__(self, name, description, scenarios):
        self.name = name
        self.description = description
        self.scenarios = scenarios
