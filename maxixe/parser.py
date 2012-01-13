import re

from . import gherkin

feature_match = re.compile(r"^Feature: (.*)$", flags=re.I)


def parse_feature(feature_string):
    feature_lines = feature_string.split("\n")
    name = feature_match.match(feature_lines.pop(0)).groups()[0]
    description = []
    for l in feature_lines:
        l = l.strip()
        if l == "":
            break
        description.append(l)
    scenarios = [gherkin.Scenario(), ]
    return gherkin.FeatureType(name, "\n".join(description), scenarios)
