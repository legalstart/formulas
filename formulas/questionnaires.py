from formulas import *

class Questionnaire(object):

    def __init__(self, name, formulas):
        self.name = name
        self.formulas = formulas

q1 = Questionnaire('q1', (formula1, formula2))
q2 = Questionnaire('q2', (formula2, formula3))
