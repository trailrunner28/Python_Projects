#!/usr/local/bin/python3

import random

user_action = None
possible_actions = ['rock', 'paper', 'scissors']
user_winner = 0
computer_winner = 0

while True:
    
    while user_action not in possible_actions:
        user_action = input('Enter a choice (rock, paper, scissors): ')
    
        computer_action = random.choice(possible_actions)
    
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
       
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == 'rock':
        if computer_action == "scissors":
            user_winner += 1
            print('Rock smashed scissors! You win!')
        else:
            computer_winner += 1
            print('Paper covers rock! You lose.')
    elif user_action == 'paper':
        if computer_action == 'rock':
            user_winner += 1
            print('Paper covers rock! You win!')
        else:
            computer_winner += 1
            print('Scissors cut paper! You lose.')
    elif user_action == 'scissors':
        if computer_action == "paper":
            user_winner += 1
            print('Scissors cut paper! You win!')
        else:
            computer_winner += 1
            print('Rock smashed scissors! You lose.')
    play_again = input('Play again? (y/n): ')
    if play_again.lower() == 'y':
        user_action = input('Enter a choice (rock, paper, scissors): ')
    else:
        print("Thanks for Playing!")
        break
        