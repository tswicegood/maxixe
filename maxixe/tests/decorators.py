import random
import unittest

from .. import decorators
from .. import registry


class StubStep(object):
    def __init__(self, description):
        self.description = description


class StepDecoratorTestCase(unittest.TestCase):
    def get_stub_step(self):
        description = "some random match %d" % random.randint(1000, 2000)
        return StubStep(description)

    def test_decoratored_function_is_put_in_registry(self):
        def foo(*args, **kwargs):
            pass

        step = self.get_stub_step()
        self.assertFalse(registry.find(step), msg="santiy check")

        decorators.step(step.description)(foo)
        self.assertEqual(registry.find(step), foo)
