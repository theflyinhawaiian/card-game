class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getScore(self):
        score = 0
        numAces = 0
        for card in self.cards:
            if card.rank == 1:
                numAces = numAces + 1
                score = score + 1
            elif card.rank > 10:
                score = score + 10
            else:
                score = score + card.rank

        for i in range(numAces):
            if score < 12:
                score += 10

        return score

    def isBusted(self):
        return self.getScore() > 21

    def hasBlackjack(self):
        return self.getScore() == 21 and len(self.cards) == 2

    def trashHand(self):
        self.cards = []
