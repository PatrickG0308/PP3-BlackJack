import random
import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)



def clear_terminal():
    """
    Clear terminal function
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_valid_name():
    """
    Welcome message and input player name and store it
    """
    print('***  Welcome to BlackJack ***')
    while True:
        name = input(Fore.GREEN +"Please enter your name (min 3 characters no spaces): ")
        if name.isalpha() and len(name) >= 3:
            return name
        print(Fore.RED +"Invalid input. Name must contain at least 3 letters.")


def main():
    """
    Menu options to view instructions or start the game
    """
    while True:
        print("Please choose an option:")
        print("1. View Instructions")
        print("2. Start Game")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            clear_terminal()
            print("Instructions: \n")
            print("1. The player and dealer are both dealt two cards")
            print("2. The player will get both cards face up")
            print("3. Dealer will have one card hidden")
            print("4. The goal of the game is to get as close"
                  "to 21 without going over")
            print("5. Player will be given the option to Hit"
                  "or Stand during your turn")
            print("6. Once you are satisfied with your score"
                  "and stand then its the dealers turn")
            print("7. The dealer must hit and draw a card on"
                  "16 but stand on 17")
            print("8. If the dealer goes over 21 he loses and you win")
            print("9. If both yourself and the dealer do not"
                  "exceed 21 then the closest to 21 wins")
            print("10. Game can end in a tie if both scores are the same")
            print("11. Scores will be reported at the end of the game \n")

        elif choice == "2":
            clear_terminal()
            play_blackjack()
            break
        else:
            print(Fore.RED +"Invalid choice. Please enter a valid option (1 or 2).")


def get_card_value(card):
    """
    Apply value to cards
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)


def get_hand_value(hand):
    """
    Apply hand value
    """
    value = sum(get_card_value(card) for card in hand)
    num_aces = hand.count('A')
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value


def print_hand(hand):
    print(" ".join(hand), "(Value:", get_hand_value(hand), ")")


def play_blackjack():
    """
    Black jack game wins losses list set to 0
    """
    wins = 0
    losses = 0

    while True:
        """
        Shuffle of deck prior to dealing
        """
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                'J', 'Q', 'K', 'A'] * 4
        random.shuffle(deck)
        """
        Dealing of 2 cards to player and dealer
        """
        player_hand = []
        dealer_hand = []
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        """
        Final round once player has decided to stand or hit then
        the remaining dealer card is shown and scores can then
        be calculated
        """
        print(Fore.GREEN +f"{username}'s hand:")
        print_hand(player_hand)
        print(Fore.MAGENTA +"Dealer's hand:")
        print(dealer_hand[0], "X")
        while get_hand_value(player_hand) < 21:
            action = input("Do you want to hit (h) or stand (s)? ").lower()
            if action in ['h', 'hit']:
                player_hand.append(deck.pop())
                print(Fore.GREEN +f"{username}'s hand:")
                print_hand(player_hand)
            elif action in ['s', 'stand']:
                print(Fore.GREEN +f"{username} stands.")
                break
            else:
                print(Fore.RED +"Invalid input. Please enter 'h' or 's'.")
        """
        If player hand greater than 17 then dealer takes another card
        """
        player_value = get_hand_value(player_hand)
        while get_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())

        print(Fore.MAGENTA +"\nDealer's hand:")
        print_hand(dealer_hand)
        """
        Calculation to determine winner of game
        """
        dealer_value = get_hand_value(dealer_hand)
        if player_value == 21:
            print(Fore.GREEN +"***Blackjack*** Congratulations, you win!")
            wins += 1
        elif player_value > 21 or (dealer_value <= 21 and
                                   dealer_value > player_value):
            print(Fore.RED +"Sorry, you lose!")
            losses += 1
        elif dealer_value > 21 or player_value > dealer_value:
            print(Fore.GREEN +"Congratulations, you win!")
            wins += 1
        else:
            print("It's a tie!")
        """
        Play Again Request
        """
        play_again = input('Do you want to play again (y/n)? ').lower()
        if play_again != 'y':
            clear_terminal()
            print(Fore.YELLOW +f"{username}, you won {wins} games and lost {losses} games.")
            print(Fore.CYAN +f'Thank you for playing {username}')
            break
        else:
            clear_terminal()


if __name__ == "__main__":
    username = get_valid_name()
    print(f"Welcome to your game of BlackJack {username}!")
    main()

