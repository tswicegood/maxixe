from maxixe.api import *


@step(r"there is a feature$")
def step_one(*args, **kwargs):
    pass


@step(r"I attempt to import that feature like a Python file")
def step_two(*args, **kwargs):
    pass


@step(r"I can access it as a module")
def step_three(*args, **kwargs):
    pass
