from main import Player, Board, MonopolyGame


def test_init_many_players():
    num_of_players = 4
    players = [Player() for _ in range(num_of_players)]
    board = Board()
    game = MonopolyGame(board)
    game.add_players(players)

    assert all(board.get_player_position(p) == board.start_square for p in players)
