# TODO: make this thread safe
import re


_registry = []


def add(match, func):
    _registry.append({
        "match": match,
        "regex": re.compile(match),
        "func": func,
    })


def find(step):
    for d in _registry:
        if d["regex"].search(step.description):
            return d["func"]
    return False