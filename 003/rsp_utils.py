import random

valid_selection = ["rock", "paper", "scissors"]

def open_text_file(file_name) -> str:
    with open(file_name) as f:
        return f.read()
    
def get_user_selection() -> str:
    return input("Enter a choice (rock, paper, scissors): ")

def get_computer_selection() -> str:
    return random.choice(valid_selection)

def check_valid_selection(user_choice) -> bool:
    return user_choice in valid_selection

def determine_the_winner(user_choice, computer_choice):
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

