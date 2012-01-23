import unittest

import maxixe
from maxixe.tests import decorators
from maxixe.tests import loader
from maxixe.tests import parser
from maxixe.tests import utils

suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromModule(decorators))
suite.addTests(unittest.TestLoader().loadTestsFromModule(loader))
suite.addTests(unittest.TestLoader().loadTestsFromModule(parser))
suite.addTests(unittest.TestLoader().loadTestsFromModule(utils))
