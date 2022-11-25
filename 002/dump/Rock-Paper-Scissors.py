import random
from rsp_utils import *

show_intro()

while True:
    possible_actions = ["rock", "paper", "scissors"]
    user_action = input("Enter a choice (rock, paper, scissors): ")

    if user_action in possible_actions:
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!\n")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!\n")
            else:
                print("Paper covers rock! You lose!\n")
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!\n")
            else:
                print("Scissors cuts paper! You lose.\n")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win.\n")
            else:
                print("Rock smashes scissors! You lose.\n")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            print(f"{user_name}, thank you for playing the 'Rock-Paper-Scissors'! See you soon ^_^")
            break
    else:
        print(f"{user_name}, please, enter the correct form word.")
        continue