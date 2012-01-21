# TODO: move to decorators
def step(match):
    def outer(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
        return inner
    return outer
