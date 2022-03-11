#!/usr/bin/env python

import random


game_point = int(input("How many points to win? "))
player_count = 0
computer_count = 0

def computer_choice():
    choice_list = ["r", "p", "s"]
    return random.choice(choice_list)

def player_choice():
    return input("Choose Rock(r) Paper(p) or Scissors(s): ")

def logic(player, computer):
    global player_count, computer_count
    print(f"You chose {player} and Computer chose {computer}")
    if computer == player:
        print("---------------")
        print("Its a Tie!")
    elif computer == "r" and player != "p":
        print("---------------")
        print("Computers Point")
        computer_count += 1
    elif computer == "p" and player != "s":
        print("---------------")
        print("Computers Point")
        computer_count += 1
    elif computer == "s" and player != "r":
        print("---------------")
        print("Computers Point")
        computer_count += 1
    else:
        print("---------------")
        print("Your Point")
        player_count += 1

def winner_check():
    global player_count, computer_count
    if computer_count == game_point:
        print("---------------")
        print("Computer Wins!")
        print("---------------")
        computer_count = 0
        player_count = 0
        cont = input("Play Again? (y or n) ")
        if cont == "n":
            exit()
        run()

    elif player_count == game_point:
        print("---------------")
        print("Player Wins")
        print("---------------")
        computer_count = 0
        player_count = 0
        cont = input("Play Again? (y or n) ")
        if cont == "n":
            exit()
        run()


def run():
    global player_count, computer_count
    while True:
        logic(player_choice(), computer_choice())
        print(f"Current score:\nPlayer {player_count} | Computer {computer_count}")
        print("---------------")
        winner_check()
run()