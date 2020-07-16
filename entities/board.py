from entities.square import Square, square_factory
from entities.bank import Bank


class Board():

    DEFAULT_BOARD_SIZE = 40

    def __init__(self, board_size=DEFAULT_BOARD_SIZE, board=None):
        self.bank = Bank()

        if not board:
            self._build_board(board_size)
        else:
            self._parse_board(board)

    @property
    def board_size(self):
        return len(self._squares)

    def _build_board(self, board_size):
        self._squares = [Square(i) for i in range(board_size)]
        self.start_square = self._squares[0]

    def traverse(self, current_square, amount):
        index = self._squares.index(current_square)
        new_index = (index + amount) % self.board_size
        return self._squares[new_index]

    def get_square_by_name(self, name):
        """
        name:   <str>
        """
        for s in self._squares:
            if str(s) == name:
                return s
        assert False, 'Square {} does not exist on this board'.format(name)

    def _parse_board(self, board):
        self._squares = [square_factory(i, self) for i in board['squares']]
        self.start_square = self._squares[0]
