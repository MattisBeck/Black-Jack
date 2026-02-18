import os
import time
from BlackJackPlayer import BlackJackPlayer, Dealer
from deck import Deck

def print_game_state(dealer:Dealer, player_list:list[BlackJackPlayer]) -> None:
    os.system("clear")
    dealer.show_all_cards()
    print("\n")
    for player in player_list:
        player.show_all_cards()
        print("\n")

    return None
def deal_all_players(player_list:list[BlackJackPlayer], deck:Deck) -> None:
    for player in player_list:
        player.pull_card(deck)

def lost():
    print("You Lost!\n" * 2)
    print("Try again")
    input("Press any key to continue...")

def won(card_value: int) -> None:
    print(f"You Won! You got {card_value if card_value < 21 else 'BlackJack'}!")
    print("You are a professional gambler!")
    input("Press any key to continue...")

def tie():
    print(f"You Tied!")

if __name__ == '__main__':
    while True:
        # Initialize New Deck
        game_deck = Deck()
        game_deck.shuffle()
        # Create Dealer and Player
        d1 = Dealer()
        p1 = BlackJackPlayer()

        #Create list of players
        players = [p1]

        deal_all_players(players, game_deck)
        d1.pull_card(game_deck)
        print_game_state(d1, players)

        time.sleep(3)
        deal_all_players(players, game_deck)
        d1.pull_card(game_deck)
        print_game_state(d1, players)

        # Player Logic
        while True:
            skip = False
            #Instant win by Dealer?
            if d1.check_blackjack():
                skip = True
                d1.first_round = False
                time.sleep(3)
                print_game_state(d1, players)
                lost()
                break
            # Instant win by Player?
            if p1.check_blackjack():
                skip = True
                d1.first_round = False
                time.sleep(1)
                print_game_state(d1, players)
                won(p1.get_hand_value())
                break
            #User Action
            print(" (0) Give Up \n (1) Hit \n (2) Stand")
            try:
                user_input = int(input("Your choice: "))
                if user_input not in range(0, 3):
                    raise ValueError
            except ValueError:
                print("Please enter a number between 0 and 2.")
                continue

            if user_input == 0:
                skip = True
                break
            elif user_input == 1:
                p1.pull_card(game_deck)
                print_game_state(d1, players)
                if p1.busted():
                    d1.first_round = False
                    time.sleep(3)
                    print_game_state(d1, players)
                    lost()
                    skip = True
                    break
                elif p1.check_blackjack():
                    d1.first_round = False
                    time.sleep(3)
                    print_game_state(d1, players)
                    won(p1.get_hand_value())
                    skip = True
                    break
                else:
                    continue
            else:
                break

        # Dealer Logic
        # Skip is true when game is already lost
        if skip:
            continue
        # Dealer has to hit he has at least cards of value 17
        d1.first_round = False
        print_game_state(d1, players)
        while d1.must_hit():
            d1.pull_card(game_deck)
            time.sleep(3)
            print_game_state(d1, players)
        # Evaluate winner
        if d1.get_hand_value() > 21:
            won(p1.get_hand_value())
        # Dealer is closer to 21 than player
        elif (21 - d1.get_hand_value()) < (21 - p1.get_hand_value()):
            lost()
        # Tie
        elif d1.get_hand_value() ==  p1.get_hand_value():
            tie()

        else:
            won(p1.get_hand_value())