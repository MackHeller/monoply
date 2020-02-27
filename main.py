import random

NAMES = ['Seb', 'Gordon', 'Mack', 'Abdule']


class MonopolyGame():

    def __init__(self, board):
        self.players = []
        self.board = board

    def add_players(self, players):
        self.players += players
        for p in players:
            self.board.add_player(p)

    def roll_die(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def run(self, rounds=20):
        for i in range(rounds):
            print('Round {}'.format(i + 1))
            for active_player in players:
                print('Player {}`s turn'.format(active_player.name))
                print('Start Square: {}'.format(board.get_player_position(active_player)))
                roll = self.roll_die()
                board.advance_player(active_player, roll)
                print('Player {} rolled {}'.format(active_player.name, roll))
                print('End Square: {}'.format(board.get_player_position(active_player)))
                print('\n')
            print('---------------------------------------\n')


class Board():

    DEFAULT_BOARD_SIZE = 40

    def __init__(self, board_size=DEFAULT_BOARD_SIZE):
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
        """
        name:   <str>
        """
        for s in self._squares:
            if str(s) == name:
                return s
        assert False, 'Square {} does not exist on this board'.format(name)


class Player():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Square():

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return str(self.id)


if __name__ == '__main__':
    players = [Player(name) for name in NAMES]
    board = Board()
    game = MonopolyGame(board)
    game.add_players(players)
    game.run()
