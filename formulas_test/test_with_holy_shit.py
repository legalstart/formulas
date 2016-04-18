from unittest import TestCase
from test_lib import class_dec, to_tesst
from formulas.rules import RULESETS

# new method using small TestCase hack
@class_dec(RULESETS)
class TestFormula(TestCase):

    @to_tesst
    def check_formula(self, rule):
        self.assertEqual(True, rule[0] not in rule[1]['formula'])

    @to_tesst
    def check_nb_input(self, rule):
        self.assertEqual(True, len(rule[1]['formula']) > 0)
