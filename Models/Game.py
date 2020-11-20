from Models.Hand import Hand
from Models.Deck import Deck


class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer_hand = Hand()
        self.player_hand = Hand()

    def start(self):
        self.deck.shuffle()
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def put_cards_back(self):
        for card in self.dealer_hand.cards:
            self.deck.add_card_on_bottom(card)
        for card in self.player_hand.cards:
            self.deck.add_card_on_bottom(card)
        self.dealer_hand.cards = []
        self.player_hand.cards = []
        self.dealer_hand.value = self.player_hand.value = 0
        self.dealer_hand.aces = self.player_hand.aces = 0
