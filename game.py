from model.deck import Deck

deck = Deck()

hand = []

while len(hand) < 10:
    hand.append(deck.dealCard())

for card in hand:
    print(card.getDisplayString())
