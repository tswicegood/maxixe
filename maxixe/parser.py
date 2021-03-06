import re
import textwrap

from . import gherkin

feature_match = re.compile(r"^Feature: (.*)$", flags=re.I)
scenario_match = re.compile(r"^Scenario: (.*)$", flags=re.I)


def parse_feature(feature_string):
    l = feature_string.split("\n\n")
    feature_string, scenario_strings = l[0], l[1:]
    feature_lines = feature_string.split("\n")
    name = feature_match.match(feature_lines.pop(0)).groups()[0]
    description = []
    for l in feature_lines:
        l = l.strip()
        if l == "":
            break
        description.append(l)
    feature = gherkin.FeatureType(name, "\n".join(description))
    feature.scenarios = [parse_scenario(a, feature) for a in scenario_strings]
    return feature


def parse_scenario(scenario_string, feature):
    scenario_lines = textwrap.dedent(scenario_string).split("\n")
    name = scenario_match.match(scenario_lines.pop(0)).groups()[0]
    scenario = gherkin.Scenario(name, feature)
    scenario.steps = [gherkin.Step(a.strip(), scenario) for a in scenario_lines
            if a.strip() != ""]
    return scenario
