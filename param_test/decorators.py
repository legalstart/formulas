from sys import modules
import inspect


def currying(elem):
    """
    Decorator for currying  a function.
    f: (x, y) ->f(x, y) is transformed into g: x->f(x, elem)
    :param elem:
    :return:
    """
    def func_decorator(func):
        def func_wrapper(self):
            return func(self, elem)
        return func_wrapper
    return func_decorator


def to_tesst(desc):
    """
    decorator for methods needing to be parametrized
    :param desc: description of what the method intends to test. It will appear
    in the error messages
    :return:
    """
    def func_decorator(func):
        func.__to_test__ = 1
        num_line = func.func_code.co_firstlineno
        func.__test_name__ = "(l%d): \"%s\" on <testable_obj>" % (
            num_line, desc)
        return func
    return func_decorator


def retrieve_test_methods(klass):
    """
    For a given class, retrieve all the methods which need to be parametrized,
    ie all the methods which have been decorated with to_tesst
    :param klass:
    :return:
    """
    methods = inspect.getmembers(klass, predicate=inspect.ismethod)
    return [m[1] for m in methods if hasattr(m[1], '__to_test__')]


def class_dec(testable_lists):
    """
    decorate a class which contains test methods which need to be parametrized
    with testable_lists
    :param testable_lists:
    :return:
    """
    def class_decorator(klass):
        test_methods = retrieve_test_methods(klass)
        for testable_list in testable_lists:
            attrs = {'testable_list': testable_list}
            for m in test_methods:
                for testable_obj in testable_list:
                    decorated_m = currying(testable_obj)(m)
                    decorated_m.__test__ = 1
                    test_name = m.__test_name__.replace(
                        "<testable_obj>", str(testable_obj))
                    attrs[test_name] = decorated_m

            tl_test_klass = type("Test_%s" % testable_list.name, (klass,),
                                 attrs)
            setattr(modules[klass.__module__], tl_test_klass.__name__,
                    tl_test_klass)
        return klass
    return class_decorator
