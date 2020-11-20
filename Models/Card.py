class Card:
    def __init__(self, suit, rank, code, value):
        self.suit = suit
        self.rank = rank
        self.code = code
        self.value = value

    def __str__(self):
        return self.rank + ' of ' + self.suit + ' (' + str(self.value) + ')'
