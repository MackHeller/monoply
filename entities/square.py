def square_factory(square):
    SquareClass = TYPE_TO_SQUARE[square['type']]
    return SquareClass(**square['attrs'])

class Square():

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', '')

    def __str__(self):
        return str(self.name)


class PropertySquare(Square):

    def __init__(self, *args, **kwargs):
        self.rent = kwargs.pop('rent', 0)
        self.price = kwargs.pop('price', 0)
        super().__init__(**kwargs)


class GoSquare(Square):
    def __init__(self, *args, **kwargs):
        super().__init__(name='go', **kwargs)


TYPE_TO_SQUARE = {
    'property': PropertySquare,
    'go': GoSquare
}

