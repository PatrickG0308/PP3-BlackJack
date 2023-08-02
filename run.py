import random
import os

# Clear terminal function


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message and input player name and store it


def get_valid_name():
    print('***  Welcome to BlackJack ***')
    while True:
        name = input("Please enter your name (minimum 3 characters): ")
        if name.isalpha() and len(name) >= 3:
            return name
        print("Invalid input. Name must contain at least 3 letters.")

# Welcome player to their game of BlackJack using obtained player name


if __name__ == "__main__":
    username = get_valid_name()
    print(f"Welcome to your game of BlackJack {username}!")
