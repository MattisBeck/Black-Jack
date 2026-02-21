class BlackJackPlayer:
    card_to_value = {
        11: 10,
        12: 10,
        13: 10,
        #14 = Ace; It is either a one or eleven, it gets implemented in get_hand_value
        14: 11
    }
    _next_id = 0

    def __init__(self):
        self.hand = []
        self.role = "Player"
        self.id = BlackJackPlayer._next_id
        BlackJackPlayer._next_id += 1

    def clear_hand(self) -> None:
        self.hand = []
        return None

    def pull_card(self, deck) -> None:
        self.hand.append(deck.deal())

    @staticmethod
    def _correct_card_value(card) -> int:
        return BlackJackPlayer.card_to_value.get(card.get_value(), card.get_value())

    def get_hand_value(self) -> int:
        num_eleven_aces = 0
        hand_value = 0
        for card in self.hand:
            value = BlackJackPlayer._correct_card_value(card)
            hand_value += value
            if value == 11:
                num_eleven_aces += 1
        # Make Aces count as 1, while hand_value > 21, then check again
        while hand_value > 21 and num_eleven_aces > 0:
            hand_value -= 10
            num_eleven_aces -= 1
        return hand_value

    def busted(self):
        return self.get_hand_value() > 21

    def check_blackjack(self):
        return self.get_hand_value() == 21

    def get_hand_str(self) -> str:
        """
        get the hand of the player
        :return: Hand of the player as a string
        """
        all_cards_by_line = [str(card).split("\n") for card in self.hand]
        return "\n".join(["  ".join(row) for row in zip(*all_cards_by_line)])

    def get_raw_hand(self):
        return self.hand


class Dealer(BlackJackPlayer):

    def __init__(self):
        super().__init__()
        self.first_round = True
        self.role = "Dealer"

    def must_hit(self):
        return self.get_hand_value() < 17

    def get_hand_str(self) -> str:
        """
        get the hand of the player
        :return: Hand of the player as a string
        """
        # Override method to hide second dealer card
        all_cards_by_line = [str(card).split("\n") for card in self.hand]
        if self.first_round and len(self.hand) >= 2:
            all_cards_by_line[1] = [f"┌───────────┐", f"│.?. . . . .│", f"│. . . . . .│", f"│. . . . . .│", f"│. . ??? . .│",
                            f"│. . . . . .│", f"│. . . . . .│", f"│. . . . .?.│", f"└───────────┘"]
        return "\n".join(["  ".join(row) for row in zip(*all_cards_by_line)])
