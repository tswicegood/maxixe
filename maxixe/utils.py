import imp

from . import registry


def module_to_feature(module):
    return "%s.feature" % "/".join(module.split(".")[-1:])


def has_matching_step(step):
    try:
        args = imp.find_module("steps", step.scenario.feature.__path__)
        if args:
            steps_mod = "%s.steps" % step.scenario.feature.__name__
            imp.load_module(steps_mod, *args)
            if registry.find(step):
                return True
    except ImportError, e:
        pass
    return False
