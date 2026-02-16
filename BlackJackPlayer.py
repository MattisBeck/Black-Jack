from tokenize import blank_re


class BlackJackPlayer:
    card_to_value = {
        11: 10,
        12: 10,
        13: 10,
        #14 = Ace; It is either a one or eleven, it gets implemented in get_hand_value
        14: 11
    }
    def __init__(self):
        self.hand = []
        self.hand_value = 0
    def pull_card(self, deck) -> None:
        self.hand.append(deck.deal())

    @staticmethod
    def _correct_card_value(card) -> int:
        return BlackJackPlayer.card_to_value.get(card.get_value(), card.get_value())

    def get_hand_value(self) -> int:
        #self.hand_value = sum(BlackJackPlayer._correct_card_value(card) for card in self.hand)
        num_eleven_aces = 0
        self.hand_value = 0
        for card in self.hand:
            value = BlackJackPlayer._correct_card_value(card)
            self.hand_value += value
            if value == 11:
                num_eleven_aces += 1
        # Make Aces count as 1, while self.hand_value > 21, then check again
        while self.hand_value > 21 and num_eleven_aces > 0:
            self.hand_value -= 10
            num_eleven_aces -= 1

        return self.hand_value