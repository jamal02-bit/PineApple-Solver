import random


class DeckUtil:

    def __init__(self, deck):
        """
        Constructor
        """
        self.deck = deck

    def parse(self, cards):
        """
        parse() parses the user input, removes cards from the deck,
                and adds to the hand.

        Args:
            cards (str): The user input card string to parse

        Returns:
            List[str]: The user input hand.
        """
        hand = cards.split(",")

        for card in hand:
            self.deck.remove(card)

        return hand

    def generateRandom(self, numberOfCards):
        """
        generateRandom() generates a random hand based on number of cards

        Args:
            numberOfCards (int): The number of cards to randomly select

        Returns:
            List[str]: The randomly generated hand
        """
        hand = []

        for _ in range(numberOfCards):
            card = random.choice(self.deck.getCards())
            hand.append(card)
            self.deck.remove(card)
        
        return hand
