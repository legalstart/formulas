class RuleSet(object):

    __slots__ = (
        'name',  # str
        'rules'  # ordered iterable
    )

    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
