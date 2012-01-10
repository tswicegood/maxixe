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
