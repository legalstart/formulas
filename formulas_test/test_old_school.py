from unittest import TestCase
from formulas import *


# First testing method : we write a test by formula
# Can quickly become repitive if many formulas
class TestFormula(TestCase):

    def check_formula(self,formula):
        return formula[0] not in formula[1][1]

    def test_formula1(self):
        self.assertEqual(True, self.check_formula(formula1))

    def test_formula2(self):
        self.assertEqual(True, self.check_formula(formula2))

    def test_formula3(self):
        self.assertEqual(True, self.check_formula(formula3))
