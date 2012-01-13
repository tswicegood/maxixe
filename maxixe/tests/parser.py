import unittest

from .. import parser

basic = """
Feature: This is a feature
  In order to understand the system under test
  As a developer and a business user
  I want to be able to parse features
""".strip()

lower = """
feature: This is a feature
  In order to understand the system under test
  As a developer and a business user
  I want to be able to parse features
""".strip()

upper = """
FEATURE: This is a feature
  In order to understand the system under test
  As a developer and a business user
  I want to be able to parse features
""".strip()

leet = """
FeaTuRe: This is a feature
  In order to understand the system under test
  As a developer and a business user
  I want to be able to parse features
""".strip()


class FeatureNameParsingTestCase(unittest.TestCase):
    expected = "This is a feature"

    def assert_expected_name(self, feature):
        self.assertEqual(feature.name, self.expected)

    def test_can_parse_feature_name(self):
        self.assert_expected_name(parser.parse_feature(basic))

    def test_can_parse_feature_with_lowercase_name(self):
        self.assert_expected_name(parser.parse_feature(lower))

    def test_can_parse_feature_with_uppercase_name(self):
        self.assert_expected_name(parser.parse_feature(upper))

    def test_can_parse_feature_with_weird_caps_name(self):
        self.assert_expected_name(parser.parse_feature(leet))
