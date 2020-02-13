
class MonopolyGame():

    def __init__(self, board):
        self.players = []
        self.board = board

    def add_players(self, players):
        self.players += players
        for p in players:
            self.board.add_player(p)


class Board():

    def __init__(self, board_size=40):
        self._build_board(board_size)
        self._positions = {}

    @property
    def board_size(self):
        return len(self._squares)

    def _build_board(self, board_size):
        self._squares = [Square(i) for i in range(board_size)]
        self.start_square = self._squares[0]

    def add_player(self, player):
        self._positions[player] = self.start_square

    def get_player_position(self, player):
        return self._positions[player]

    def advance_player(self, player, amount):
        current_square = self.get_player_position(player)
        index = self._squares.index(current_square)
        new_index = (index + amount) % self.board_size
        new_square = self._squares[new_index]
        self.move_player_to_square(player, new_square)

    def move_player_to_square(self, player, square):
        self._positions[player] = square

    def get_square_by_name(self, name):
        for s in self._squares:
            if s.name == name:
                return s
        assert False, 'Square {} does not exist on this board'.format(name)


class Player():

    def __init__(self):
        pass


class Square():

    def __init__(self, id):
        self.id = id

    @property
    def name(self):
        return str(self.id)


if __name__ == '__main__':
    num_of_players = 4
    players = [Player() for _ in range(num_of_players)]
    board = Board()
    game = MonopolyGame(board)
    game.add_players(players)
