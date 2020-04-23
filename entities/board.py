from entities.square import Square


class Board():

    DEFAULT_BOARD_SIZE = 40

    def __init__(self, board_size=DEFAULT_BOARD_SIZE):
        self._build_board(board_size)

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
