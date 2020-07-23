from entities.property import Property

def square_factory(square, board):
    SquareClass = TYPE_TO_SQUARE[square['type']]
    return SquareClass(board=board, **square['attrs'])

class Square():

    def __init__(self, **kwargs):
        self.board = kwargs.pop('board')
        self.name = kwargs.pop('name', '')

    def __str__(self):
        return str(self.name)

    def take_action(self, active_player):
        raise NotImplementedError


class PropertySquare(Square):

    def __init__(self, *args, **kwargs):
        price = kwargs.pop('price', 0)
        rent = kwargs.pop('rent', 0)
        super().__init__(**kwargs)
        self.property = Property(self.board.bank, price, rent)

    def take_action(self, active_player):
        if self.property.owner == self.board.bank:
            self.property.sell_to(active_player, self.property.price)
        else:
            raise NotImplementedError


class GoSquare(Square):
    def __init__(self, *args, **kwargs):
        super().__init__(name='go', **kwargs)

    def take_action(self, active_player):
        self.board.bank.pay(active_player, 200)


TYPE_TO_SQUARE = {
    'property': PropertySquare,
    'go': GoSquare
}
