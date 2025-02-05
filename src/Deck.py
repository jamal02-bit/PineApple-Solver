class Deck:
    suits = "shdc"
    ranks = "AKQJT98765432"

    def __init__(self):
        """
        Contructor
        """
        cards = []
        for r in Deck.ranks:
            for s in Deck.suits:
                cards.append(r + s)
        self.cards = cards
    
    def remove(self, card):
        """
        remove() Removes cards from the deck.

        Args:
            card (str): The card to remove.
        """
        self.cards.remove(card)

    def __str__(self):
        """
        toString() function
        """
        return f"Deck: {self.cards}"
    
    def getCards(self):
        """
        getCards() Getter function to return the cards array

        Returns:
            List[str]: The cards in the deck.
        """
        return self.cards
