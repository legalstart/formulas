from unittest import TestCase
from formulas import *
from test_lib import holy_shit


# new method using small TestCase hack
# problems : cannot use other method call in decorated method
# ....
class TestFormula(TestCase):

    formula_tuple = (formula1, formula2, formula3)

    @holy_shit(formula_tuple)
    def check_formula(self, formula):
        self.assertEqual(True, formula[0] not in formula[1][1])