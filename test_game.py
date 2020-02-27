from main import Player, Board, MonopolyGame


def test_init_many_players():
    num_of_players = 4
    players = [Player(str(i)) for i in range(num_of_players)]
    board = Board()
    game = MonopolyGame(board)
    game.add_players(players)

    assert all(p.position == board.start_square for p in players)


def test_traverse():
    board = Board()
    assert board.traverse(board.start_square, 4) == board.get_square_by_name('4')


def test_traverse_past_start_square():
    board = Board()
    assert board.traverse(board.start_square, Board.DEFAULT_BOARD_SIZE + 4) == board.get_square_by_name('4')


def test_move_player():
    board = Board()
    game = MonopolyGame(board, dice_function= lambda: 5)
    player = Player('Seb')
    game.add_players([player])
    game.move_player(player)
    assert str(player.position) == '5'


def test_two_rounds():
    board = Board()
    player = Player('Seb')
    game = MonopolyGame(board, dice_function=lambda: 5)
    game.add_players([player])
    game.run(rounds=2)
    assert player.position == board.get_square_by_name('10')

