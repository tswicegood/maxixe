from __builtin__ import __import__
from os.path import exists
from os.path import join
import os
import re
import sys
from types import ModuleType


feature_match = re.compile(r"^[Ff]eature: (.*)$")

def parse_feature(feature_string):
    feature_lines = feature_string.split("\n")
    name = feature_match.match(feature_lines.pop(0)).groups()[0]
    description = []
    for l in feature_lines:
        l = l.strip()
        if l == "":
            break
        description.append(l)
    scenarios = [Scenario(), ]
    return FeatureType(name, "\n".join(description), scenarios)


class FeatureFinder(object):
    """
    .. todo:: Find permanent home for this
    """
    def find_module(self, fullname, path=None):
        # A feature is never a top level module, so return immediately
        if path is None:
            return
        from .utils import module_to_feature
        feature_name = module_to_feature(fullname)
        for p in path:
            feature = join(p, feature_name)
            if exists(feature):
                return FeatureLoader(feature)
        return None


class FeatureLoader(object):
    def __init__(self, feature):
        self.feature = feature

    def load_module(self, fullname):
        with open(self.feature) as f:
            return parse_feature(f.read())



class Scenario(object):
    def __init__(self):
        self.name = "Found feature"
        self.steps = (1, 2, 3, )


class FeatureType(ModuleType):
    def __init__(self, name, description, scenarios):
        self.name = name
        self.description = description
        self.scenarios = scenarios


def init():
    sys.meta_path.append(FeatureFinder())
