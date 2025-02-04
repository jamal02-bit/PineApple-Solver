from src.Deck import Deck

class DeckUtil:

    def __init__(self):
        self.deck = Deck()

    def parse(self, cards):
        split_cards = cards.split(",")

        for card in split_cards:
            self.deck.remove(card)

        print(self.deck)
        print(split_cards)

        return split_cards

    def generateRandom(self, numberOfCards):
        pass

