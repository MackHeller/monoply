from abc import abstractmethod


class Transactable():

    @abstractmethod
    def pay(self, payee, amount):
        raise NotImplementedError

    @abstractmethod
    def receive(self, amount):
        raise NotImplementedError
