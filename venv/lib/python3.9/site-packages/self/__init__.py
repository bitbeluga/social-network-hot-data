__all__ = ['self']


import inspect
from decorator import decorator


def self(method, self, *args, **kwargs):
    """`@self` method decorator to return self object"""
    if not inspect.isroutine(method):
        err = "@self decorator for methods only, got %s" % method
        raise TypeError(err)
    margs = [self] + list(args)
    r = method(*margs, **kwargs)
    if r:
        raise ValueError("@self %s result is not None" % method)
    return self
