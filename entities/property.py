class Property():

    def __init__(self, owner):
        self.owner = owner

    def transfer_to(self, player):
        self.owner = player
