import random

user_name = input("Enter your name: ")
print("\n\tRock-Paper-Scissors is a hand game, usually played between two people, in which\neach player simultaneously forms one of three shapes with an outstretched hand.\nThese shapes are 'rock' (a closed fist), 'paper' (a flat hand),and 'scissors' (a fist with\nthe index finger and middle finger extended, forming a 'V').\n\nIt has three possible outcomes: a tie, a win or a loss. A player who decides\nto play 'rock' will win another player who has chosen scissors ('rock smashes scissors'),\nbut will lose to one who has played paper ('paper covers rock'). A play of paper will lose\nto a play of scissors ('scissors cuts paper'). If both players choose the same shape,\nthe game is tied and is usually immediately replayed to break the tie.")
print(f"\n{user_name}, let's play!\n")

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