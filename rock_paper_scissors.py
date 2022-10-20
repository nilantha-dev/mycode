#!/usr/bin/env python3

"""Alta3 labs |nilantha| rock, paper, scissors game"""

# imports random
import random

def main():
    """Cycle through multiple oppertunities to play"""
    while True:
        #getting input from the user and make it lower case
        user_choice = input('Select rock, paper, scissors(select something else to exit the game):').lower()
        #display the user choice
        print("You chose: " + user_choice)
        array = ['rock','paper','scissors']
        #getting system choice in the array at random
        system_choice = random.choice(array)
        #display system choice
        print("System chose: " + system_choice)
        #comparing user choice and system choice to determine and display win or loose
        if user_choice == system_choice:
            print("It's a tie")
        elif user_choice == 'rock' and system_choice == 'paper':
            print("You loose")
        elif user_choice == 'rock' and system_choice == 'sissors':
            print("You win")
        elif user_choice == 'paper' and system_choice == 'rock':
            print("You win")
        elif user_choice == 'paper' and system_choice == 'scissors':
            print("You loose")
        elif user_choice == 'scissors' and system_choice == 'rock':
            print("You loose")
        elif user_choice == 'scissors' and system_choice == 'paper':
            print("You win")
        else:
            print("Thanks for playing!")
            #prevent an infinite loop
            break
if __name__ == "__main__":
    main()
