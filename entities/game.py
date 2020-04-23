import random


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
            print('---------------------------------------\n')
