import imp


def module_to_feature(module):
    return "%s.feature" % "/".join(module.split(".")[-1:])


def has_matching_step(step):
    # TODO: must load .steps, register all matching, then check those
    try:
        imp.find_module("steps", step.scenario.feature.__path__)
        return True
    except ImportError, e:
        return False
