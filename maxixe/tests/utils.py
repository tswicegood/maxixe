import unittest

from .. import utils


class module_to_feature_TestCase(unittest.TestCase):
    def test_converts_module_name_to_feature_name(self):
        module = "foo.basics"
        feature = utils.module_to_feature(module)
        self.assertEqual("basics.feature", feature)
