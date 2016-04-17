from unittest import TestCase
from formulas import *


# Second testing method, for loop in test
# two problems :
#   1 : in case of failure the error message won't be explicit
#   2 : the test will stop as soon as one test fails
class TestFormula(TestCase):

    formula_tuple = (formula1, formula2, formula3)

    def check_formula(self,formula):
        return formula[0] not in formula[1][1]

    def test_formulas(self):
        for formula in TestFormula.formula_tuple:
            self.assertEqual(True, self.check_formula(formula))