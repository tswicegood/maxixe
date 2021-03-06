import textwrap
import unittest

from .. import parser


FEATURES = {
    "basic": """
Feature: This is a feature
  In order to understand the system under test
  As a developer and a business user
  I want to be able to parse features
""".strip(),

    "lower": """
feature: This is a feature
  In order to understand the system under test
  As a developer and a business user
  I want to be able to parse features
""".strip(),

    "upper": """
FEATURE: This is a feature
  In order to understand the system under test
  As a developer and a business user
  I want to be able to parse features
""".strip(),

    "leet": """
FeaTuRe: This is a feature
  In order to understand the system under test
  As a developer and a business user
  I want to be able to parse features
""".strip(),
}


class FeatureNameParsingTestCase(unittest.TestCase):
    expected = "This is a feature"

    def parse_feature(self, name):
        return parser.parse_feature(FEATURES[name])

    def assert_expected_name(self, feature):
        self.assertEqual(feature.name, self.expected)

    def test_can_parse_feature_name(self):
        self.assert_expected_name(self.parse_feature("basic"))

    def test_can_parse_feature_with_lowercase_name(self):
        self.assert_expected_name(self.parse_feature("lower"))

    def test_can_parse_feature_with_uppercase_name(self):
        self.assert_expected_name(self.parse_feature("upper"))

    def test_can_parse_feature_with_weird_caps_name(self):
        self.assert_expected_name(self.parse_feature("leet"))


class FeatureDescriptionTestCase(unittest.TestCase):
    def to_description(self, s):
        return textwrap.dedent(s).strip()

    def test_can_parse_feature_description(self):
        self.assertEqual(self.to_description("""
            In order to understand the system under test
            As a developer and a business user
            I want to be able to parse features
        """), parser.parse_feature(FEATURES["basic"]).description)

SCENARIOS = {
    "basic": """
Scenario: Basic scenario
  Given that I have a few steps
  When I parse that scenario
  Then I have a full Scenario object
""".strip(),

    "lower": """
scenario: Basic scenario
  Given that I have a few steps
  When I parse that scenario
  Then I have a full Scenario object
""".strip(),

    "upper": """
SCENARIO: Basic scenario
  Given that I have a few steps
  When I parse that scenario
  Then I have a full Scenario object
""".strip(),

    "leet": """
SCeNaRio: Basic scenario
  Given that I have a few steps
  When I parse that scenario
  Then I have a full Scenario object
""".strip(),
}


class ScenarioNameParsingTestCase(unittest.TestCase):
    expected = "Basic scenario"
    expected_feature = parser.parse_feature(FEATURES["basic"])

    def parse_scenario(self, name):
        return parser.parse_scenario(SCENARIOS[name], feature=self.expected_feature)

    def assert_expected_name(self, scenario):
        self.assertEqual(scenario.feature, self.expected_feature,
                msg="sanity check")
        self.assertEqual(scenario.name, self.expected)

    def test_can_parse_feature_name(self):
        self.assert_expected_name(self.parse_scenario("basic"))

    def test_can_parse_scenario_with_lowercase_name(self):
        self.assert_expected_name(self.parse_scenario("lower"))

    def test_can_parse_scenario_with_uppercase_name(self):
        self.assert_expected_name(self.parse_scenario("upper"))

    def test_can_parse_scenario_with_weird_caps_name(self):
        self.assert_expected_name(self.parse_scenario("leet"))


class ScenarioStepParsingTestCase(unittest.TestCase):
    expected_feature = parser.parse_feature(FEATURES["basic"])

    def get_parsed_scenario(self):
        scenario = parser.parse_scenario(SCENARIOS["basic"], feature=self.expected_feature)
        return scenario

    def test_can_parse_steps(self):
        scenario = self.get_parsed_scenario()
        self.assertEqual(3, len(scenario.steps))

    def test_steps_are_what_is_parsed(self):
        scenario = self.get_parsed_scenario()
        self.assertEqual("Given that I have a few steps", scenario.steps[0].description)
        self.assertEqual("When I parse that scenario", scenario.steps[1].description)
        self.assertEqual("Then I have a full Scenario object", scenario.steps[2].description)

    def test_steps_are_all_marked_as_not_run_by_default(self):
        scenario = self.get_parsed_scenario()
        for step in scenario.steps:
            self.assertFalse(step.has_run,
                    msg="Step [%s] has been run?" % step.description)

    def test_steps_are_marked_as_not_runnable_by_default(self):
        scenario = self.get_parsed_scenario()
        for step in scenario.steps:
            self.assertFalse(step.runnable,
                    msg="Step [%s] is runnable?" % step.description)
