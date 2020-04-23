from entities.board import Board
from entities.player import Player
from entities.game import MonopolyGame


NAMES = ['Seb', 'Gordon', 'Mack', 'Abdul', 'Mo']

if __name__ == '__main__':
    players = [Player(name) for name in NAMES]
    board = Board()
    game = MonopolyGame(board)
    game.add_players(players)
    game.run()
