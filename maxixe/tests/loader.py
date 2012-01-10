import unittest


class FeatureFinderTestCase(unittest.TestCase):
    def setUp(self):
        import maxixe
        maxixe.init()

    def test_loads_name_from_file(self):
        from maxixe.features import basics
        self.assertEqual(basics.name, "Importable features")
