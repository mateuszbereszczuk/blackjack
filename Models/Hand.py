class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def is_hand_over(self):
        return True if self.value > 21 else False
