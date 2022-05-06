import random

class Card:
    """
    Individual cards are represented as a number from 1 to 13.

    Attributes:
        value (int): The number of the different cards.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def draw(self):
        """Generates a new random value for the Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
