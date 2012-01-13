from __builtin__ import __import__
from os.path import exists
from os.path import join
import os
import re
import sys

from . import parser
from .gherkin import FeatureType
from .gherkin import Scenario


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
            return parser.parse_feature(f.read())


def init():
    sys.meta_path.append(FeatureFinder())
