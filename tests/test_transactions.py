import pytest

from entities.player import Player
from entities.bank import Bank
from entities.property import Property


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


def test_cannot_go_into_negative_balance():
    p1 = Player('tester', 40)
    p2 = Player('tester', 100)
    with pytest.raises(AssertionError):
        p1.pay(p2, 60)
    assert p1.balance == 40
    assert p2.balance == 100


# def test_transfer_property():
    # b = Bank()
    # prop = Property(owner=b)
    # p = Player('tester', 100)

    # assert prop.owner == b

    # prop.transfer_to(b, p)

    # assert prop.owner == p


def test_buy_sell_property():
    b = Bank()
    prop = Property(owner=b)
    p = Player('tester', 100)

    assert prop.owner == b

    prop.sell_to(p, 60)

    assert p.balance == 40
    assert prop.owner == p


def test_cannot_sell_property_if_buyer_balance_insufficient():
    b = Bank()
    prop = Property(owner=b)
    p = Player('tester', 40)

    with pytest.raises(AssertionError):
        prop.sell_to(p, 60)

    assert p.balance == 40
    assert prop.owner == b


def test_can_pay_rent():
    p1 = Player('tester', 100)
    p2 = Player('tester', 100)
    prop = Property(owner=p1, rent=60)

    prop.pay_rent()

    assert p1.balance == 160
    assert p2.balance == 40
