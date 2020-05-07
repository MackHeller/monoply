from abc import abstractmethod


class Transactable():

    @abstractmethod
    def pay(self, payee, amount):
        raise NotImplementedError

    @abstractmethod
    def receive(self, amount):
        raise NotImplementedError

    def sell_to(self, player, property_, price):
        player.pay(self, price)
        property_.transfer_to(player)
