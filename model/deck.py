from random import randint
from model.card import Card

class Deck:
    def __init__(self):
        self.dealtCards = []

    def generateCard(self):
        return Card(randint(1,13), randint(1,4))

    def dealCard(self):
        card = self.generateCard()
        while card in self.dealtCards:
            card = self.generateCard()

        self.dealtCards.append(card)
        return card
