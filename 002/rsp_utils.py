import random

possible_actions = ["rock", "paper", "scissors"]
user_name = ""

def set_user_name(name) :
    global user_name
    user_name = name

def load_text_file(file_name)->str:
    with open(file_name) as f:
        return f.readlines()

def show_intro():
    # user_name = input("Enter your name: ")
    # print("\n\tRock-Paper-Scissors is a hand game, usually played between two people, in which\neach player simultaneously forms one of three shapes with an outstretched hand.\nThese shapes are 'rock' (a closed fist), 'paper' (a flat hand),and 'scissors' (a fist with\nthe index finger and middle finger extended, forming a 'V').\n\nIt has three possible outcomes: a tie, a win or a loss. A player who decides\nto play 'rock' will win another player who has chosen scissors ('rock smashes scissors'),\nbut will lose to one who has played paper ('paper covers rock'). A play of paper will lose\nto a play of scissors ('scissors cuts paper'). If both players choose the same shape,\nthe game is tied and is usually immediately replayed to break the tie.")
    print(load_text_file('./res/intro.txt'))

def define_user() -> str:
    return input("Enter your name: ")


def get_user_input() -> str:
    # possible_actions = ["rock", "paper", "scissors"]
    return input("Enter a choice (rock, paper, scissors): ")


def check_choice_valid(choice) -> bool:
    return choice in possible_actions


def get_computer_choice():
    return random.choice(possible_actions)


def show_play_result():
    print("show_play_result")


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

        user_action = get_user_input()

        if check_choice_valid(user_action):
            computer_action = get_computer_choice()
            print(f"\nYou chose {user_action}, computer chose {computer_action}.")
            determine_result(user_action, computer_action)

        else:
            print(f"{user_name}, please, enter the correct form word.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            print(
                f"{user_name}, thank you for playing the 'Rock-Paper-Scissors'! See you soon ^_^")
            break
