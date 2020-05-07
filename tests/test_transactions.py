import pytest

from entities.player import Player, InsufficientFundsError
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
    with pytest.raises(InsufficientFundsError):
        p1.pay(p2, 60)
    assert p1.balance == 40
    assert p2.balance == 100


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

    with pytest.raises(InsufficientFundsError):
        prop.sell_to(p, 60)

    assert p.balance == 40
    assert prop.owner == b


def test_can_collect_rent():
    p1 = Player('tester', 100)
    p2 = Player('tester', 100)
    prop = Property(owner=p1, rent=60)

    prop.collect_rent(p2)

    assert p1.balance == 160
    assert p2.balance == 40


def test_cannot_pay_rent_raises_exception():
    p1 = Player('tester', 100)
    p2 = Player('tester', 40)
    prop = Property(owner=p1, rent=60)

    with pytest.raises(InsufficientFundsError):
        prop.collect_rent(p2)

    assert p1.balance == 100
    assert p2.balance == 40


def test_can_mortgage_property():
    b = Bank()
    p1 = Player('tester', 100)
    prop = Property(owner=p1, price=120)
    assert prop.is_mortgaged is False

    prop.mortgage(b)

    assert p1.balance == 160
    assert prop.is_mortgaged is True


def test_cannot_double_mortgage_property():
    b = Bank()
    p1 = Player('tester', 100)
    prop = Property(owner=p1)

    prop.mortgage(b)
    with pytest.raises(AssertionError):
        prop.mortgage(b)


def test_mortgaged_property_charges_no_rent():
    pass


def test_can_repay_mortgage():
    b = Bank()
    p1 = Player('tester', 100)
    prop = Property(owner=p1, price=120)
    prop._mortgaged = True

    prop.unmortgage(b)

    assert p1.balance == 40
    assert prop.is_mortgaged is False
