import uuid 
import random
from .game_exceptions import InvalidGameInput


class MontyHallGame(object):
    """ Instantiates a new Monty Hall Game object.

    Example usage:

    ```
    game = MontyHallGame()

    game.select_door(1)
    game.let_host_open_door()

    to_open = random.choice(game.available_doors())
    game.select_door(to_open)

    won = game.open_door()
    ```

    """


    stats = {
             "changed":     {"won": 0, "lost": 0},
             "not_changed": {"won": 0, "lost": 0}
            }

    @staticmethod
    def statistics():
        """ Returns statistics about the winning chances of the "change door" 
        and "do not change door" strategies of all games played. """


        # Get statistics class variable
        stats = MontyHallGame.stats

        s1 = "Changed and won: {} out of {}".format(
                stats["changed"]["won"], 
                stats["changed"]["won"] + stats["changed"]["lost"]
                )

        s2 = "Not changed and won: {} out of {}".format(
                stats["not_changed"]["won"], 
                stats["not_changed"]["won"] + stats["not_changed"]["lost"]
                )

        return "{}\n{}".format(s1, s2)


    def __init__(self):
        self.game_id = str(uuid.uuid4())

        self.__winning_door = random.randint(1, 3)
        self.selected_door = None
        self.opened_door = None
        self.reselected_door = None


    def select_door(self, door):
        """ Use this function to let the play select a door. This function
        should be called twice: Once at the beginning of the game for the initial
        door choice. And once after calling :function:`MontyHallGame.let_host_open_door`.
        
        :ivar door: The door to be selected. Valid values: [1, 2, 3]
        """

        if not 1 <= door <= 3:
            raise InvalidGameInput("Door must be an integer between 1 and 3, you provided {}.".format(door))

        if door == self.opened_door:
            raise InvalidGameInput("Cannot select opened door")

        if self.selected_door is None:
            self.selected_door = door
        else:
            self.reselected_door = door


    def available_doors(self):
        """ Returns a list of doors that are still available for selection """


        a = set([1, 2, 3])
        a.discard(self.opened_door) 
        return list(a)


    def let_host_open_door(self):
        """ When this function is called, the host will open a door that contains no price.

        :returns: The newly opened door number as an int. """

        if self.selected_door is None:
            raise InvalidGameInput("You must first select a door")

        if self.opened_door is not None:
            raise InvalidGameInput("The host has already opened a door")

        opened = set([1, 2, 3])
        opened.discard(self.__winning_door)
        opened.discard(self.selected_door)
        self.opened_door = random.choice(list(opened))

        return self.opened_door


    def open_door(self):
        """ Opens the door selected by the player 

        :returns: `True` if the player has won, `False` otherwise. """

        if self.reselected_door is None or self.opened_door is None:
            raise InvalidGameInput("You must select a door after letting the host open a door.")

        changed = self.selected_door != self.reselected_door
        game_won = self.reselected_door == self.__winning_door

        # Update statistics
        if changed:
            if game_won:
                MontyHallGame.stats["changed"]["won"] += 1
            else:
                MontyHallGame.stats["changed"]["lost"] += 1
        if not changed:
            if game_won:
                MontyHallGame.stats["not_changed"]["won"] += 1
            else:
                MontyHallGame.stats["not_changed"]["lost"] += 1

        return game_won

if __name__ == "__main__":
    game = MontyHallGame()

    game.select_door(1)
    game.let_host_open_door()

    to_open = random.choice(game.available_doors())
    game.select_door(to_open)

    won = game.open_door()

    if won:
        print("You won")
    else:
        print("You lost")
