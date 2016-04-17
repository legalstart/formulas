from unittest import TestCase
from sys import modules


def currying(elem):
    def func_decorator(func):
        def func_wrapper(self):
            return func(self, elem)
        return func_wrapper
    return func_decorator


# small hack to enable iteration on test methods
def holy_shit(iterable, klass_name="holy_shit"):
    def func_decorator(func):
        klass = type(klass_name, (TestCase,), {})

        for i, elem in enumerate(iterable):
            test_name = "test_%s_%d" % (func.__name__, i + 1)
            check = currying(elem)(func)
            check.__test__ = 1
            setattr(klass, test_name, check)
        setattr(modules[func.__module__], "current_test",  klass)
    return func_decorator

