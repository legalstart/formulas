import __builtin__
from unittest import TestCase
from param_test import class_dec, to_tesst
from formulas.lib import undefined_vars
from formulas.rules import RULESETS
from formulas.rules_list import EVAL_CONTEXT_BASE


_BASE_VARS_SET = \
    set(dir(__builtin__)) | set(EVAL_CONTEXT_BASE.iterkeys()) | {'_'}


# new method using small TestCase hack
@class_dec(RULESETS)
class TestFormula(TestCase):

    def __init__(self, *args, **kwargs):
        self._all_vars = self.testable_list.initial_vars
        super(TestFormula, self).__init__(*args, **kwargs)

    @to_tesst('rule syntax is well-formed')
    def check_syntax(self, rule):
        """ rule is a 2ple like ``(varname, {'type': ..., 'formula': ...})``
        """
        self.assertEqual(len(rule), 2)
        self.assertTrue('formula' in rule[1],
                        msg="Rule doesn't contain a formula")
        self.assertTrue('type' in rule[1],
                        msg="Rule doesn't contain a type")

    @to_tesst('all formula inputs already exist')
    def check_inputs_exist(self, rule):
        """ In the rule formula, are the expected inputs really available?
        Launched on every varname in the right order.
        """
        formula = rule[1]['formula']
        formula_input_vars = undefined_vars(formula)

        # All the availabe varnames: augmented w/ previously calculated varnames
        available_vars = set(self._all_vars) | _BASE_VARS_SET

        self.assertTrue(formula_input_vars.issubset(available_vars),
                        msg=("Formula expects vars that don't exist: %s"
                             % ', '.join(formula_input_vars - available_vars)))

        # Add the calculated varname
        self._all_vars.append(rule[0])
