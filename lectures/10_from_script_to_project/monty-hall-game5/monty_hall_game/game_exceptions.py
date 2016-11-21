class InvalidGameInput(Exception):
    """ This exception should be thrown if invalid input is provided to the 
    game. An example is to finish the game before selecting a door. """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
