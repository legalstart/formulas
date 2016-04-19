class TestableList(list):
    """list of objects to be parametrized for tests"""

    __slots__ = (
        'name',  # str
    )

    def __init__(self, name, l=None):
        self.name = name
        if l is None:
            super(TestableList, self).__init__()
        else:
            super(TestableList, self).__init__(l)
