from src.Deck import Deck
import random

class DeckUtil:

    def __init__(self):
        self.deck = Deck()

    def parse(self, cards):
        hand = cards.split(",")

        for card in hand:
            self.deck.remove(card)

        return hand

    def generateRandom(self, numberOfCards):
        hand = []
        
        for i in range(numberOfCards):
            card = random.choice(self.deck.getCards())
            hand.append(card)
            self.deck.remove(card)
        
        return hand