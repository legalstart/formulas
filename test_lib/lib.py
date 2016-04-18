from unittest import TestCase
from sys import modules
import inspect


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


def to_tesst(func):
    func.__to_test__ = 1
    return func


def retrieve_test_methods(klass):
    methods = inspect.getmembers(klass, predicate=inspect.ismethod)
    return [m[1] for m in methods if hasattr(m[1], '__to_test__')]


def class_dec(questionnaires):
    def class_decorator(klass):
        test_methods = retrieve_test_methods(klass)
        for q in questionnaires:
            attrs = {}
            for m in test_methods:
                for i, f in enumerate(q.formulas):
                    decorated_m = currying(f)(m)
                    decorated_m.__test__ = 1
                    test_name = "test_%s_on_formula_%d" % (m.__name__, i + 1)
                    attrs[test_name] = decorated_m

            q_test_klass = type("test_%s" % q.name, (klass,), attrs)
            setattr(modules[klass.__module__], q_test_klass.__name__,
                    q_test_klass)
    return class_decorator
