class RuleSet(object):

    __slots__ = (
        'name',  # str
        'rules'  # list or tuple
    )

    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
