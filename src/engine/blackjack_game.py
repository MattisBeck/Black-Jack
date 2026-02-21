from enum import Enum

from players import BlackJackPlayer, Dealer
from deck import Deck


class PlayerStatus(Enum):
    BUSTED = 0
    BLACKJACK = 1
    SAFE = 2


class BlackjackGame:
    def __init__(self, dealer: Dealer, player_list: list[BlackJackPlayer], deck: Deck):
        self._dealer = dealer
        self._player_list = player_list
        self._deck = deck

    def _deal_all_players_start(self) -> None:
        for player in self._player_list:
            player.pull_card(self._deck)

    def _deal_dealer_start(self) -> None:
        self._dealer.pull_card(self._deck)

    def deal_dealer_end(self) -> None:
        while self._dealer.must_hit():
            self._dealer.pull_card(self._deck)

    def deal_round_start(self):
        self._deal_all_players_start()
        self._deal_dealer_start()
        # Do this twice to start first round

    def player_hit(self, i: int) -> PlayerStatus:
        """
        Deals a player a card and checks if it busted
        :param i: index of the player
        :return: PlayerStatus representing the player
        """
        self._player_list[i].pull_card(self._deck)
        if self._player_list[i].get_hand_value() > 21:
            return PlayerStatus.BUSTED
        elif self._player_list[i].get_hand_value() == 21:
            return PlayerStatus.BLACKJACK
        else:
            return PlayerStatus.SAFE

    def get_game_state(self) -> list[tuple[int, list, int]]:
        """
        fetches current game state
        :return: hands the dealer and all players tuples inside a list in
        the following order: (player_index (-1 if dealer), hand (printable), hand_value)
        """
        dealer = (-1, self._dealer.get_raw_hand(), self._dealer.get_hand_value())
        return [dealer] + [(i, player.get_raw_hand(), player.get_hand_value()) for i, player in
                           enumerate(self._player_list)]
