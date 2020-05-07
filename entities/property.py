class Property():

    def __init__(self, owner):
        self.owner = owner

    def sell_to(self, current_owner, acquiror, price):
        assert self.owner == current_owner
        acquiror.pay(current_owner, price)
        self.owner = acquiror
