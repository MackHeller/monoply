from main import Player, Board, MonopolyGame


def test_init_many_players():
    num_of_players = 4
    players = [Player(str(i)) for i in range(num_of_players)]
    board = Board()
    game = MonopolyGame(board)
    game.add_players(players)

    assert all(board.get_player_position(p) == board.start_square for p in players)


def test_advance_player():
    board = Board()
    player = Player('Bob')
    board.add_player(player)
    assert board.get_player_position(player) == board.start_square
    board.advance_player(player, 4)
    assert board.get_player_position(player) == board.get_square_by_name('4')


def test_advance_player_past_start_square():
    board = Board()
    player = Player('Seb')
    board.add_player(player)
    assert board.get_player_position(player) == board.start_square
    board.advance_player(player, Board.DEFAULT_BOARD_SIZE + 4)
    assert board.get_player_position(player) == board.get_square_by_name('4')


def test_move_player():
    board = Board()
    player = Player('Seb')
    board.add_player(player)
    assert board.get_player_position(player) == board.start_square
    board.move_player_to_square(player, board.get_square_by_name('10'))
    assert board.get_player_position(player) == board.get_square_by_name('10')
