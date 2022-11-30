from rsp_utils import *
from settings import *

print(open_text_file(get_intro_file_location()))

load_game_model()

set_user_name(define_user())

while True:
    user_choice = get_user_selection()

    if check_valid_selection(user_choice):
        computer_choice = get_computer_selection()
        determine_the_winner(user_choice, computer_choice)      
    else:
        print("Please, enter the correct form word.")
        continue

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thank you for playing the 'Rock-Paper-Scissors'! See you soon ^_^")
        break