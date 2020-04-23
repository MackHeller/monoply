from entities.player import Player
from entities.bank import Bank


def test_player_to_bank():
    p = Player('tester', 100)
    b = Bank()
    p.pay(b, 100)
    assert p.balance == 0


def test_bank_to_player():
    p = Player('tester', 100)
    b = Bank()
    b.pay(p, 100)
    assert p.balance == 200


def test_player_to_player():
    p1 = Player('tester', 100)
    p2 = Player('tester', 100)
    p1.pay(p2, 100)
    assert p1.balance == 0
    assert p2.balance == 200
