import random

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

"""Representation of cards"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value  = VALUES[rank]

    def getCardValue(self):
        return self.value

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.won = "None"
        self.player1 = ""
        self.player2 = ""
        self.player1cards = []
        self.player2cards = []
        self.turn = ""
        self.lastPlayedTime = 0

    def __str__(self):
        p1cards = "["
        for cards in self.player1cards:
            p1cards += str(cards) + ","
        p1cards += "]"
        p2cards = "["
        for cards in self.player2cards:
            p2cards += str(cards) + ","
        p2cards += "]"

        return "Game id:" + self.game_id+ "\n Player1: "+ str(self.player1)+" with picked cards:" +p1cards+ ".\n" \
               "Player2: " +str(self.player2)+" with picked cards:" +p2cards+ ".\n Current Player Turn: " + str(self.turn)+" \n Won:" + str(self.won)


"""Deck (list) of cards"""
class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        res = "["
        for index, card in enumerate(self.deck):
            res += str(card)
            if index < len(self.deck) - 1:
                res += ", "
        return res + "]"

    """Shuffle the cards"""
    def shuffle(self):
        random.shuffle(self.deck)

    """ Size of remaining deck """
    def size(self):
        return len(self.deck)

    """Remove card from the top of deck
    :return card"""
    def pick(self):
        return self.deck.pop()

    def pickColor(self, color):
        if color == "RED":
            for i in range(len(self.deck)):
                if self.deck[i].suit == 'Hearts' or self.deck[i].suit == 'Diamonds':
                    return self.deck.pop(i)
        else:
            for i in range(len(self.deck)):
                if self.deck[i].suit == 'Spades' or self.deck[i].suit == 'Clubs':
                    return self.deck.pop(i)
        return None

    def pickSuite(self, suit):
        for i in range(len(self.deck)):
            if self.deck[i].suit == suit:
                return self.deck.pop(i)
        return None
