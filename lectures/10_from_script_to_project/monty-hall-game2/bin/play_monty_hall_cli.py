#!/usr/bin/env python

from monty_hall_game import MontyHallGame, InvalidGameInput

while True:
    try:
        print("\n\nWelcome to a new Monty Hall game")
        print("******************************\n")

        game = MontyHallGame()

        door = int(input("Select a door between 1-3: "))
        game.select_door(door)

        door = game.let_host_open_door()
        print("The host opens door {}.".format(door))

        a = game.available_doors()
        door = int(input("Which door would you like to open (choose from {}): ".format(a)))

        game.select_door(door)
        won = game.open_door()

        if won:
            print("Congratulations! You have won!")
        else:
            print("I am sorry! You have lost.")

        print("\n---------------")
        print("Game statistics")
        print("---------------")
        print(game.statistics())

    except InvalidGameInput as e:
        print(e)
        print("Restarting game...")
