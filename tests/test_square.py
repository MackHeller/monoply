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
    players = [Player('Mack')]
    board = Board(board=SQUARES)

    game = MonopolyGame(board, dice_function=lambda: 1)
    game.add_players(players)

    property_square = game.board._squares[1]

    assert players[0].position == game.board.start_square
    assert property_square.property.owner == game.board.bank

    game.move_player(players[0])
    game.take_action(players[0])

    assert players[0].position == property_square
    assert property_square.property.owner == players[0]

def test_collect_money_on_pass_go():
    assert False, 'start here'