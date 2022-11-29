import random
from rsp_utils import *


user_name = input("Enter your name: ")

# print(open_text_file(r'./res/intro.txt'))
# print(open_text_file(r'D:\works\project\Rock-Paper-Scissors\003\res\intro.txt'))
print(open_text_file(r'.\003\res\intro.txt'))

print(f"\n{user_name}, let's play!\n")

while True:
    user_choice = get_user_selection()

    if check_valid_selection(user_choice):
        computer_choice = get_computer_selection()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
        determine_the_winner(user_choice, computer_choice)      
    else:
        print(f"{user_name}, please, enter the correct form word.")
        continue
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print(f"{user_name}, thank you for playing the 'Rock-Paper-Scissors'! See you soon ^_^")
        break