class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False

        return self.rank == other.rank and self.suit == other.suit

    def getDisplayRank(self):
        if(self.rank >= 2 and self.rank <= 10):
            return str(self.rank)

        match (self.rank):
            case 1:
                return "A"
            case 11:
                return "J"
            case 12:
                return "Q"
            case 13:
                return "K"
            case _:
                return "?"

    def getDisplaySuit(self):
        match(self.suit):
            case 1:
                return "Diamonds"
            case 2:
                return "Spades"
            case 3:
                return "Hearts"
            case 4:
                return "Clubs"

    def getDisplayString(self):
        return f"{self.getDisplayRank()} of {self.getDisplaySuit()}"
