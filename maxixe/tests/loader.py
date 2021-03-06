import os
import unittest


class FeatureFinderTestCase(unittest.TestCase):
    def setUp(self):
        import maxixe
        maxixe.init()

    def test_loads_name_from_file(self):
        from maxixe.features import basics
        self.assertEqual(basics.name, "Importable features")

    def test_loads_description_from_file(self):
        from maxixe.features import basics
        expected = "\n".join([
            "In order to interact programmatically with tests",
            "Developers should be able to import features as code",
        ])
        self.assertEqual(basics.description, expected)

    def test_has_a_scenario_list_with_length_of_scenarios(self):
        from maxixe.features import basics
        contents = open(os.path.join(basics.__path__[0],
                "basics.feature")).read()
        expected_scenarios = len([1 for a in contents.split("\n")
                if a.strip().lower().startswith("scenario:")])
        self.assertEqual(len(basics.scenarios), expected_scenarios)

    def test_scenario_is_fleshed_out(self):
        import maxixe
        from maxixe.features import basics
        scenario = basics.scenarios[0]
        self.assertTrue(isinstance(scenario, maxixe.Scenario))
        self.assertEqual(scenario.name, "Found feature")
        self.assertEqual(len(scenario.steps), 3)

    def test_feature_has_correct_parent_module(self):
        from maxixe.features import basics
        self.assertEqual(basics.__name__, "maxixe.features")

    def test_first_scenario_is_runnable(self):
        from maxixe.features import basics
        self.assertTrue(basics.scenarios[0].runnable)

    def test_second_scenario_is_runnable(self):
        from maxixe.features import basics
        self.assertTrue(basics.scenarios[1].runnable)

    def test_third_scenario_is_not_runnable_since_first_step_is_unknown(self):
        from maxixe.features import basics
        scenario = basics.scenarios[2]
        self.assertFalse(scenario.runnable)

    def test_empty_scenario_is_not_runnable(self):
        from maxixe.features import basics
        self.assertFalse(basics.scenarios[3].runnable)
