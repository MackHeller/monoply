class Player():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position
