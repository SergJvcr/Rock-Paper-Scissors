import random
import json
from settings import *

user_name = ""
valid_selection = []
valid_selection_2 = {}
game_status_model = []

def set_user_name(name):
    global user_name
    user_name = name

def define_user() -> str:
    return input("Enter your name: ")

def open_text_file(file_name) -> str:
    with open(file_name) as f:
        return f.read()

def load_json_object(file_name):
    with open(file_name) as f:
        return json.load(f)

def load_game_model():
    global game_status_model
    game_status_model = load_json_object(get_model_file_location())

    global valid_selection
    global valid_selection_2
    valid_selection = []
    for status in game_status_model:
        status_name = status.get('name')
        valid_selection.append(status_name)
        valid_selection_2[status_name] = status_name
        for short in status.get('shorts'):
            valid_selection.append(short)
            valid_selection_2[short] = status_name

def get_valid_choice(choice)->str:
    return valid_selection_2.get(choice,'')

def get_user_selection() -> str:

    print(f"\n{user_name}, let's play!\n")

    s = ""
    for status in game_status_model:
        if len(s) > 0:
            s += ', '
        s += status.get('name') + '(' + str(status.get('shorts')) + ')'

    return input("Enter a choice (" + s + "): ")

def get_computer_selection() -> str:
    return random.choice(game_status_model).get('name')

def check_valid_selection(user_choice) -> bool:
    return user_choice in valid_selection

def check_status_equals(status, user_choice) ->bool:
    return status.get('name') == user_choice or user_choice in status.get('shorts')

def determine_the_winner(user_choice, computer_choice):
    for status in game_status_model:
        if check_status_equals(status, user_choice):
            if computer_choice in status.get('win'):
                print(f"Your choice: {get_valid_choice(user_choice)} VS computer choise: {get_valid_choice(computer_choice)}")
                print(f"{user_name}, you win!")
            elif computer_choice in status.get('lose'):
                print(f"Your choice: {get_valid_choice(user_choice)} VS computer choise: {get_valid_choice(computer_choice)}")
                print(f"{user_name}, you lose!")
            else:
                print(f"Both players selected {get_valid_choice(user_choice)}. It's a tie!\n")
            break