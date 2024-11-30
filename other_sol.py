import os
import random


def clear():
    os.system('cls')


struct = ""
game_on = True
chance = 0
n = ''
player_1 = 'O'
player_2 = 'X'
keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
pressed_keys = []


board = ["\n ", " ", " | ", " ", " | ", " ", "\n", "___________\n ", " ", " | ", " ", " | ",
         " ", "\n", "___________\n ", " ", " | ", " ", " | ", " "]


def grid():
    global struct
    for char in board:
        struct += char
    print(struct)


def input_key(mark):
    global chance, pressed_keys
    print(pressed_keys)
    if mark in pressed_keys:
        print("The box is already filled press another key")
        chance -= 1
    else:
        pressed_keys.append(mark)
        if mark == "9":
            board[5] = n

        elif mark == "8":
            board[3] = n

        elif mark == "7":
            board[1] = n

        elif mark == "6":
            board[12] = n

        elif mark == "5":
            board[10] = n

        elif mark == "4":
            board[8] = n

        elif mark == "3":
            board[19] = n

        elif mark == "2":
            board[17] = n

        elif mark == "1":
            board[15] = n

        else:
            print("Invalid Key")
            chance -= 1

        clear()
    grid()

def computer():
    pass


def check_rules():
    global game_on
    if board[15] == board[17] == board[19] != " ":
        print(f" player {board[15]} won")
        game_on = False

    elif board[8] == board[10] == board[12] != " ":
        print(f" player {board[8]} won")
        game_on = False

    elif board[1] == board[3] == board[5] != " ":
        print(f" player {board[1]} won")
        game_on = False

    elif board[3] == board[10] == board[17] != " ":
        print(f" player {board[3]} won")
        game_on = False

    elif board[5] == board[12] == board[19] != " ":
        print(f" player {board[5]} won")
        game_on = False

    elif board[1] == board[8] == board[15] != " ":
        print(f" player {board[1]} won")
        game_on = False

    elif board[1] == board[10] == board[19] != " ":
        print(f" player {board[1]} won")
        game_on = False

    elif board[5] == board[10] == board[15] != " ":
        print(f" player {board[10]} won")
        game_on = False

    else:
        pass

grid()

choice = input("For Multiplayer, press 'm' \nfor single player press 's': \n").lower()
clear()
if choice == 'm' or choice == 's':
    while game_on:

        chance += 1
        struct = ""

        if chance > 9:
            print("Draw")
            game_on = False

        elif chance % 2 == 0 and choice == 'm':
            n = player_1
            input_key(input(""))

        elif chance % 2 == 0 and choice == 's':
            n = player_1
            input_key(random.choice(keys))

        else:
            n = player_2
            input_key(input(""))

        check_rules()

else:
    print("press valid key")