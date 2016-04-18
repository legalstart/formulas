from unittest import TestCase
from formulas import *
from test_lib import class_dec, to_tesst


# new method using small TestCase hack
# problems : cannot use other method call in decorated method
# ....
@class_dec((q1, q2))
class TestFormula(TestCase):

    #formula_tuple = (formula1, formula2, formula3)

    @to_tesst
    def check_formula(self, formula):
        self.assertEqual(True, formula[0] not in formula[1][1])
