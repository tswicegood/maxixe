def module_to_feature(module):
    return "%s.feature" % "/".join(module.split(".")[-1:])
