import random
import json

from settings import *

# possible_actions = ["rock", "paper", "scissors"]
possible_actions = []
possible_actions2 = {}
user_name = ""
game_status_model = []


def set_user_name(name):
    global user_name
    user_name = name


def load_text_file(file_name) -> str:
    with open(file_name) as f:
        return f.readlines()


def show_intro():
    # user_name = input("Enter your name: ")
    # print("\n\tRock-Paper-Scissors is a hand game, usually played between two people, in which\neach player simultaneously forms one of three shapes with an outstretched hand.\nThese shapes are 'rock' (a closed fist), 'paper' (a flat hand),and 'scissors' (a fist with\nthe index finger and middle finger extended, forming a 'V').\n\nIt has three possible outcomes: a tie, a win or a loss. A player who decides\nto play 'rock' will win another player who has chosen scissors ('rock smashes scissors'),\nbut will lose to one who has played paper ('paper covers rock'). A play of paper will lose\nto a play of scissors ('scissors cuts paper'). If both players choose the same shape,\nthe game is tied and is usually immediately replayed to break the tie.")
    print(load_text_file(get_into_file_location()))


def load_json_object(file_name):
    with open(file_name) as f:
        return json.load(f)


def load_game_model():
    global game_status_model
    game_status_model = load_json_object(get_model_file_location())

    global possible_actions
    global possible_actions2
    possible_actions = []
    for status in game_status_model:
        sn = status.get('name')
        possible_actions.append(sn)
        possible_actions2[sn] = sn
        for short in status.get('shorts'):
            possible_actions.append(short)
            possible_actions2[short] = sn

def get_fine_choice(choice)->str:
    # return possible_actions2[choice]
    return possible_actions2.get(choice,'')
            
def define_user() -> str:
    return input("Enter your name: ")


def get_user_input() -> str:
    s = ""
    for status in game_status_model:
        if len(s) > 0:
            s += ', '
        s = s + status.get('name') + '('+str(status.get('shorts'))+')'

    return input("Enter a choice (" + s + "): ")


def check_choice_valid(choice) -> bool:
    return choice in possible_actions


def get_computer_choice():
    # return random.choice(possible_actions)
    return random.choice(game_status_model).get('name')


def show_play_result():
    print("show_play_result")

def check_status_equals(status, user_choice) ->bool:
    return status.get('name') == user_choice or user_choice in status.get('shorts')

def determine_result_2(user_choice, computer_choice):
    for status in game_status_model:
        # if (status.get('name') == user_choice):
        if (check_status_equals(status, user_choice)):
            if (computer_choice in status.get('win')):
                print('User1 win: '+get_fine_choice(user_choice)+' vs '+get_fine_choice(computer_choice))
            elif (computer_choice in status.get('lose')):
                print('User2 win: '+get_fine_choice(user_choice)+' vs '+get_fine_choice(computer_choice))
            else:
                print(f"Both players selected {get_fine_choice(user_choice)}. It's a tie!\n")

            break


def determine_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!\n")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!\n")
        else:
            print("Paper covers rock! You lose!\n")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!\n")
        else:
            print("Scissors cuts paper! You lose.\n")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win.\n")
        else:
            print("Rock smashes scissors! You lose.\n")


def play():
    print(f"\n{user_name}, let's play!\n")

    while True:

        user_choice = get_user_input()

        if check_choice_valid(user_choice):
            computer_choice = get_computer_choice()
            print(
                f"\nYou chose {user_choice}, computer chose {computer_choice}.")
            # determine_result(user_action, computer_action)
            determine_result_2(user_choice, computer_choice)

        else:
            print(f"{user_name}, please, enter the correct form word.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            print(
                f"{user_name}, thank you for playing the 'Rock-Paper-Scissors'! See you soon ^_^")
            break
