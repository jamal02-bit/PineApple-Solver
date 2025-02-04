class Deck:
    suits = "shdc"
    ranks = "AKQJT98765432"

    def __init__(self):
        cards = []
        for r in Deck.ranks:
            for s in Deck.suits:
                cards.append(r + s)
        self.cards = cards
    
    def remove(self, card):
        self.cards.remove(card)