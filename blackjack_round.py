from model.hand import Hand

class BlackjackRound:
    def __init__(self, numPlayers, deck):
        self.deck = deck
        self.hands = []
        self.dealerHand = Hand()
        self.playerBlackjacks = []

        for i in range(numPlayers):
            self.hands.append(Hand())
            self.playerBlackjacks.append(False)

    def dealHand(self):
        for i in range(len(self.hands)):
            self.hands[i].addCard(self.deck.dealCard())
            self.hands[i].addCard(self.deck.dealCard())

        self.dealerHand.addCard(self.deck.dealCard())
        self.dealerHand.addCard(self.deck.dealCard())

    def dealerHit(self):
        self.dealerHand.addCard(self.deck.dealCard())

    def hit(self, playerNum):
        self.hands[playerNum].addCard(self.deck.dealCard())

    def hasBlackjack(self, playerNum):
        return self.hands[playerNum].hasBlackjack()

    def isBusted(self, playerNum):
        return self.hands[playerNum].isBusted()

    def score(self, playerNum):
        return self.hands[playerNum].getScore()

    def printHand(self, playerNum):
        hand = self.hands[playerNum].cards
        for i in range(len(hand)):
            print(hand[i].getDisplayString())

    def printDealerHand(self):
        hand = self.dealerHand.cards
        for i in range(len(hand)):
            print(hand[i].getDisplayString())
