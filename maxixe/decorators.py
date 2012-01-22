from . import registry


def step(match):
    def outer(func):
        registry.add(match, func)
        def inner(*args, **kwargs):
            func(*args, **kwargs)
        return inner
    return outer
