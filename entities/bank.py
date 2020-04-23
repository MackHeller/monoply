from entities.transactable import Transactable


class Bank(Transactable):

    def pay(self, payee, amount):
        payee.receive(amount)

    def receive(self, amount):
        pass
