import random

def get_computer_choice():
    rps_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(rps_list)
    computer_choice = computer_choice.lower()
    return computer_choice

def get_user_choice():
    user_choice = input("Enter your input here: ")
    user_choice = user_choice.lower()
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == "scissors" and user_choice == "rock":
        print(f'You picked {user_choice}, the computer picked {computer_choice}. Congratulations!! You won the game')
    elif computer_choice == "scissors" and user_choice == "paper":
        print(f'You picked {user_choice}, the computer picked {computer_choice}. Sorry!! You lost the game')
    elif computer_choice == "rock" and user_choice == "scissors":
        print(f'You picked {user_choice}, the computer picked {computer_choice}. Sorry!! You lost the game')
    elif computer_choice == "rock" and user_choice == "paper":
        print(f'You picked {user_choice}, the computer picked {computer_choice}. Congratulations!! You won the game')
    elif computer_choice == "paper" and user_choice == "scissors":
        print(f'You picked {user_choice}, the computer picked {computer_choice}. Congratulations!! You won the game')
    elif computer_choice == "paper" and user_choice == "rock":
        print(f'You picked {user_choice}, the computer picked {computer_choice}. Sorry!! You lost the game')
    elif computer_choice == user_choice:
        print(f'You picked {user_choice}, the computer picked {computer_choice}. It is a tie!! Please try again')
    
def play_game():
    return get_winner(get_computer_choice(), get_user_choice())
play_game()