#TODO a virer
from test_lib import RuleSet
from formulas import *


class Questionnaire(RuleSet):
    pass

q1 = Questionnaire('q1', (formula1, formula2, formula4))
q2 = Questionnaire('q2', (formula2, formula3))
