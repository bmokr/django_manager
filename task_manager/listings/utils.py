from itertools import tee


def pair_iterable_for_delta_changes(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
