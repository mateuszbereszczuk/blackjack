import random
from Models.Card import Card


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = {
    'Two': ('2', 2),
    'Three': ('3', 3),
    'Four': ('4', 4),
    'Five': ('5', 5),
    'Six': ('6', 6),
    'Seven': ('7', 7),
    'Eight': ('8', 8),
    'Nine': ('9', 9),
    'Ten': ('10', 10),
    'Jack': ('J', 10),
    'Queen': ('Q', 10),
    'King': ('K', 10),
    'Ace': ('A', 11)
}


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank, value in ranks.items():
                self.deck.append(Card(suit, rank, value[0], value[1]))

    def __str__(self):
        deck_description = ''
        for card in self.deck:
            deck_description += '\n ' + card.__str__()
        return 'The deck has:' + deck_description

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def add_card_on_bottom(self, card):
        self.deck.insert(0, card)
