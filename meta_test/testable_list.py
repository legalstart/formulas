class TestableList(list):

    __slots__ = (
        'name',  # str
    )

    def __init__(self, name):
        self.name = name
