

class Property():

    _mortgaged = False

    def __init__(self, owner, price, rent):
        self.owner = owner
        self.rent = rent
        assert price % 2 == 0, 'property price must be even'
        self.price = price

    def sell_to(self, acquiror, price):
        acquiror.pay(self.owner, price)
        self.owner = acquiror

    def collect_rent(self, payee):
        if not self.is_mortgaged:
            payee.pay(self.owner, self.rent)

    def mortgage(self, bank):
        assert not self.is_mortgaged, 'Property was already mortgaged'
        bank.pay(self.owner, self.mortgage_amount)
        self._mortgaged = True

    def unmortgage(self, bank):
        assert self.is_mortgaged, 'Property was not mortgaged'
        self.owner.pay(bank, self.mortgage_amount)
        self._mortgaged = False

    @property
    def mortgage_amount(self):
        return self.price / 2

    @property
    def is_mortgaged(self):
        return self._mortgaged