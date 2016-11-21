import uuid
import random


class MontyHallGame(object):
    stats = {
             "changed":     {"won": 0, "lost": 0},
             "not_changed": {"won": 0, "lost": 0}
            }

    @staticmethod
    def statistics():

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
        if self.selected_door is None:
            self.selected_door = door
        else:
            self.reselected_door = door


    def available_doors(self):

        a = set([1, 2, 3])
        a.discard(self.opened_door)
        return list(a)


    def let_host_open_door(self):
        opened = set([1, 2, 3])
        opened.discard(self.__winning_door)
        opened.discard(self.selected_door)
        self.opened_door = random.choice(list(opened))

        return self.opened_door


    def open_door(self):

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
