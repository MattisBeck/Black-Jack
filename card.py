from enum import Enum
class Suits(Enum):
    HEARTS = "♥️"
    SPADES = "♠️"
    DIAMONDS = "♦️"
    CLUBS = "♣️"

class Ranks(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14



class Card:
    display_differs_from_value = {
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
    }
    def __init__(self, suit, rank):
        if suit not in Suits:
            raise ValueError(f'Suit {suit} is not a valid suit')
        elif rank not in Ranks:
            raise ValueError(f'Rank {rank} is not a valid rank')
        self.suit = suit
        self.rank = rank
    def __str__(self):
        r = self.rank.value
        s = self.suit.value
        if r in Card.display_differs_from_value:
            r = Card.display_differs_from_value[r]

        display_card = []
        display_card.append(f"┌───────────┐")
        display_card.append(f"│.{r}. . . . .│")
        display_card.append(f"│. . . . . .│")
        display_card.append(f"│. . ..  . .│")
        display_card.append(f"│. . .{s} . .│")
        display_card.append(f"│. . . . . .│")
        display_card.append(f"│. . . . . .│")
        display_card.append(f"│. . . . .{r}.│")
        display_card.append(f"└───────────┘")

        #Fix layout for strings with two digits
        if len(str(r)) == 2:
            display_card[1] = display_card[1].replace(f".{r}", str(r))
            display_card[7] = display_card[7].replace(f"{r}.", str(r))
        return "\n".join(display_card)
    def get_value(self):
        return self.rank.value