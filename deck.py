import random

from card import Card, Ranks, Suits
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suits for rank in Ranks]
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop()


