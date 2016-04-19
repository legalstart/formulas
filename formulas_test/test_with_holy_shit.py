import __builtin__
from unittest import TestCase
from meta_test import class_dec, to_tesst
from formulas.lib import undefined_vars
from formulas.rules import RULESETS
from formulas.rules_list import EVAL_CONTEXT_BASE


# new method using small TestCase hack
@class_dec(RULESETS)
class TestFormula(TestCase):

    def __init__(self, *args, **kwargs):
        self._all_vars = self.testable_list.initial_vars
        super(TestFormula, self).__init__(*args, **kwargs)

    @to_tesst
    def check0_syntax(self, rule):
        self.assertEqual(len(rule), 2)
        self.assertTrue('formula' in rule[1],
                        msg="Rule doesn't contain a formula")
        self.assertTrue('type' in rule[1],
                        msg="Rule doesn't contain a type")

    @to_tesst
    def check1_inputs_exist(self, rule):
        """ Launched on every varname in order """
        formula = rule[1]['formula']
        formula_input_vars = undefined_vars(formula)

        # All the availabe vars: the RulesSet initial vars augmented with
        available_vars = (
            set(self._all_vars) | set(dir(__builtin__)) |
            set(EVAL_CONTEXT_BASE.iterkeys()) | {'_'}
        )

        self.assertTrue(formula_input_vars.issubset(available_vars),
                        msg=("Formula expects vars that don't exist: %s"
                             % ', '.join(formula_input_vars - available_vars)))

        self._all_vars.append(rule[0])
