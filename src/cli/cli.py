from src.engine.blackjack_game import BlackjackGame
from src.engine.players import Dealer, BlackJackPlayer
from src.engine.deck import Deck
from src.engine.constants import TIME_BETWEEN_ACTIONS
import os


def print_game_state(state: list[tuple]) -> None:
    """
    Prints the game state to the console
    :param state: state from BlackJackGame.get_game_state()
    :return: None
    """
    # dealer_hand, player_hands = state[0], state[1:]
    ##TODO fix clearing for all operating systems
    os.system("clear")
    for player in state:
        # prints either Dealer or the players id
        print("Dealer:" if player[0] == -1 else f"Player {player[0] + 2}:")
        print(player[1])
        print(f"Hand Value: {player[2]}")


def cli():
    # Main game loop
    print("Hello!")
    while True:
        try:
            player_count = int(input("With how many players would you like to play?"))
            if 1 <= player_count <= 4:
                break
        except ValueError:
            print("Please enter a natural number between 1 and 4")
    list_of_players = [BlackJackPlayer() for _ in range(player_count)]
    while True:
        current_game = BlackjackGame(Dealer(), list_of_players, Deck())
        current_game.deal_round_start()
