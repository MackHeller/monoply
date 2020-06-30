from entities.board import Board
from entities.player import Player
from entities.game import MonopolyGame

SQUARES = {
  'squares': [
    {'type': 'go',
    'attrs': {}
    },
    {'type': 'property',
      'attrs' : {
        'name': 'Baltic Ave',
        'price': 60,
        'rent': 4,
      }
    }
  ]
}


def test_move_and_buy_property():
    assert False 'start here';
    players = [Player('Mack')]
    board = Board(board=SQUARES)

    game = MonopolyGame(board, dice_function=lambda: 1)
    game.add_players(players)
    game.move_player(players[0])
    game.take_action(player[0])


    assert all(p.position == board.start_square for p in players)