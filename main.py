
class MonopolyGame():

    def __init__(self, board):
        self.players = []
        self.board = board

    def add_players(self, players):
        self.players += players
        for p in players:
            self.board.add_player(p)


class Board():

    def __init__(self):
        self._build_board()
        self._positions = {}

    def _build_board(self):
        self.squares = [Square() for _ in range(40)]
        self.start_square = self.squares[0]

    def add_player(self, player):
        self._positions[player] = self.start_square

    def get_player_position(self, player):
        return self._positions[player]


class Player():

    def __init__(self):
        pass


class Square():

    def __init__(self):
        pass


if __name__ == '__main__':
    num_of_players = 4
    players = [Player() for _ in range(num_of_players)]
    board = Board()
    game = MonopolyGame(board)
    game.add_players(players)
