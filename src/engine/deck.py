import random
from card import Card, Ranks, Suits


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suits for rank in Ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __add__(self, other):
        if not isinstance(other, Deck):
            raise TypeError(f"Cant add a Deck to {type(other)}")
        return self.cards + other.cards
