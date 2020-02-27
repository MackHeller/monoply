import random

NAMES = ['Seb', 'Gordon', 'Mack', 'Abdule']

def roll_two_six_sided_dice():
    return random.randint(1, 6) + random.randint(1, 6)


class MonopolyGame():

    def __init__(self, board, dice_function=roll_two_six_sided_dice):
        self.players = []
        self.board = board
        self.dice_function = dice_function

    def add_players(self, players):
        self.players += players
        for p in players:
            p.position = self.board.start_square

    def roll_die(self):
        return self.dice_function()

    def move_player(self, active_player):
        print('Player {}`s turn'.format(active_player.name))
        print('Start Square: {}'.format(active_player.position))
        roll = self.roll_die()
        active_player.position = self.board.traverse(active_player.position, roll)
        print('Player {} rolled {}'.format(active_player.name, roll))
        print('End Square: {}'.format(active_player.position))
        print('\n')


    def run(self, rounds=20):
        for i in range(rounds):
            print('Round {}'.format(i + 1))
            for active_player in self.players:
                self.move_player(active_player)
            # input()
            print('---------------------------------------\n')


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


class Player():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position


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
