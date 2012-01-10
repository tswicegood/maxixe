import unittest

import maxixe
from maxixe.tests import loader
from maxixe.tests import utils

suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromModule(loader))
