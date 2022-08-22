from model.deck import Deck
from blackjack_round import BlackjackRound

deck = Deck()
cont = ""

round = BlackjackRound(4, deck)
round.dealHand()

for i in range(len(round.hands)):
    print(f"Player {i + 1}'s hand:")
    round.printHand(i)

print("Dealer's hand:")
print(round.dealerHand.cards[0].getDisplayString())
print("? of ?")

player_stands = False

if(round.hasBlackjack(0)):
    print("BLACKJACK!")
    player_stands = True

while(not round.isBusted(0) and not player_stands):
    action = input(f"Your score is {round.score(0)}. Do you want to hit (1) or stand (2)? ")
    match action:
        case "1":
            round.hit(0)
        case "2":
            player_stands = True
        case _:
            print("Bad input!")

    round.printHand(0)

    if round.isBusted(0):
        print("Busted!")

for player in range(1,len(round.hands)):
    shouldStand = False
    if(round.hasBlackjack(player)):
        print(f"Player {player+1} has blackjack!")
        shouldStand = True

    while(not round.isBusted(player) and not shouldStand):
        if(round.score(player) < 17):
            print(f"Player {player+1} hits")
            round.hit(player)
        else:
            print(f"Player {player+1} stands")
            shouldStand = True

        round.printHand(player)
        print(f"Player {player+1}'s score is {round.score(player)}.")

        if round.isBusted(player):
            print(f"Player {player+1} busted!")

        cont = input("Press Enter to continue:")

if(round.dealerHand.hasBlackjack()):
    print("The dealer has blackjack!")
    shouldStand = True

shouldStand = False
while(not round.dealerHand.isBusted() and not shouldStand):
    if(round.dealerHand.getScore() < 17):
        print(f"The dealer hits")
        round.dealerHit()
    else:
        print(f"The dealer stands")
        shouldStand = True

    round.printDealerHand()
    print(f"The dealer's score is {round.dealerHand.getScore()}.")

    if round.dealerHand.isBusted():
        print(f"The dealer busted!")

    cont = input("Press Enter to continue:")

for i in range(len(round.hands)):
    if(round.hands[i].hasBlackjack() and round.dealerHand.hasBlackjack()):
        print(f"Player {i+1} pushes.")
    elif(round.hands[i].isBusted() or (not round.dealerHand.isBusted() and round.dealerHand.getScore() >= round.hands[i].getScore())):
        print(f"Player {i+1} loses!")
    else:
        print(f"Player {i+1} wins!")
