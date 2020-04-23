from entities.transactable import Transactable


class Player(Transactable):

    def __init__(self, name, starting_balance=1500):
        self.balance = starting_balance
        self.name = name

    def __str__(self):
        return self.name

    @property
    def position(self):
        return self._position

    def pay(self, payee, amount):
        self.balance = self.balance - amount
        payee.receive(amount)

    def receive(self, amount):
        self.balance = self.balance + amount

    @position.setter
    def position(self, new_position):
        self._position = new_position
