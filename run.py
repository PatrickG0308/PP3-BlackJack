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

# Menu options to view instructions or start the game


def main():
    while True:
        print("Please choose an option:")
        print("1. View Instructions")
        print("2. Start Game")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            clear_terminal()
            print("Instructions: \n")
            print("1. The player and dealer are both dealt two cards \n")
            print("2. The player will get both cards face up and the dealer will have one card hidden. \n")
            print("3. The goal of the game is to get as close to 21 without going over (bust) \n")
            print("4. Player will be given the option to Hit or Stand during your turn \n")
            print("5. Once you are satisfied with your score and stand then its the dealers turn.\n")
            print("6. The dealer must hit and draw a card on 16 but stand on 17. \n")
            print("7. If the dealer goes over 21 he loses and you win.\n")
            print("8. If both yourself and the dealer do not exceed 21 then the closest to 21 wins \n")
            print("9. Game can end in a tie if both scores are the same \n")
            print("10. Scores are recorded and will be reported at the end of the game \n")

        elif choice == "2":
            clear_terminal()
            play_blackjack()
            break
        else:
            print("Invalid choice. Please enter a valid option (1 or 2).")

# Apply value to cards


def get_card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

# Apply hand value


def get_hand_value(hand):
    value = sum(get_card_value(card) for card in hand)
    num_aces = hand.count('A')
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value


def print_hand(hand):
    print(" ".join(hand), "(Value:", get_hand_value(hand), ")")


