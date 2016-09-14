# Problem 54
# In the card game poker, a hand consists of five cards and are ranked, from
# lowest to highest, in the following way:

# A. High Card: Highest value card.
# B. One Pair: Two cards of the same value.
# C. Two Pairs: Two different pairs.
# D. Three of a Kind: Three cards of the same value.
# E. Straight: All cards are consecutive values.
# F. Flush: All cards of the same suit.
# G. Full House: Three of a kind and a pair.
# H. Four of a Kind: Four cards of the same value.
# I. Straight Flush: All cards are consecutive values of same suit.
# J. Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives (see
# example 1 below). But if two ranks tie, for example, both players have a pair
# of queens, then highest cards in each hand are compared (see example 4
# below); if the highest cards tie then the next highest cards are compared,
# and so on.

# Consider the following five hands dealt to two players:
# -------|------------------------------------------------------|----------------------------------------------------|----------|
# Hand   | Player 1                                             |  Player 2                                          | Winner   |
# -------|------------------------------------------------------|----------------------------------------------------|----------|
# 1      | 5H 5C 6S 7S KD Pair of Fives                         | 2C 3S 8S 8D TD Pair of Eights                      | Player 2 |
# 2      | 5D 8C 9S JS AC Highest card Ace                      | 2C 5C 7D 8S QH Highest card Queen                  | Player 1 |
# 3      | 2D 9C AS AH AC Three Aces                            | 3D 6D 7D TD QD Flush  with Diamonds                | Player 2 |
# 4      | 4D 6S 9H QH QC Pair of Queens    (Highest card Nine) | 3D 6D 7H QD QS Pair of Queens (Highest card Seven) | Player 1 |
# 5      | 2H 2D 4C 4D 4S Full House        (With Three Fours)  | 3C 3D 3S 9S 9D Full House (with Three Threes)      | Player 1 |
# -------|------------------------------------------------------|----------------------------------------------------|----------|

# Player 1 The file, poker.txt, contains one-thousand random hands dealt
# to two players. Each line of the file contains ten cards (separated by a
# single space): the first five are Player 1's cards and the last five are
# Player 2's cards. You can assume that all hands are valid (no invalid
# characters or repeated cards), each player's hand is in no specific
# order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

# Sample lines from txt file
# 8C TS KC 9H 4S 7D 2S 5D 3S AC
# 5C AD 5D AC 9C 7C 5H 8D TD KS

# read in txt file into lists of tuples for [(shape), (value)]
# determine which hand is better or tie
    # convert hand to an ordered list of numbers, shape
    # rank hand from [A-J]
    # compare highest cards
# count wins for both players
import sys, re, subprocess, time, operator

class Card(object):

    SUITS = {
            'D':   'Diamonds',
            'C':   'Clubs',
            'H':   'Hearts',
            'S':   'Spades'
            }

    # Define the names of special cards
    VALUES = {
             'A' : '1',
             'T' : '10',
             'J' : '11',
             'Q' : '12',
             'K' : '13'
             }

    SPECIAL_VALUES = {
            '1': 'Ace',
            '10': '10',
            '11': 'Jack',
            '12': 'Queen',
            '13': 'King'
             }

    def __init__(self):
        self.suit_full  = None
        self.suit       = None
        self.value      = None
        self.int_value  = 0
        return

    def set_suit(self, suit):
        self.suit      = str(suit)
        self.suit_full = str(self.SUITS[suit])
        return

    def set_value(self, value):
        if value.isdigit() == True:
            self.value = str(value)
        else:
            self.value = str(self.VALUES[value])

        self.int_value = int(self.value)
        return

    def __set__(self, other):
        self.suit_full = other.suit_full
        self.suit      = other.suit
        self.value     = other.value
        self.int_value = other.int_value
        return

    def __str__(self):
        # Return a string description of ourself
        if self.value in self.SPECIAL_VALUES:
            buf = self.SPECIAL_VALUES[str(self.value)]
        else:
            buf = str(self.value)

        buf = buf + ' of ' + self.SUITS[str(self.suit)]
        return buf

    def __lt__(self, other):
        # Compare the card with another card
        # (return true if we are smaller, false if
        # we are larger, 0 if we are the same)
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False

        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False
        return 0

# hand is a set of 5 cards
class Hand(object):

    def __init__(self):
        self.cardList = [Card() for i in range(5)]

    def set_hand(self, otherCardList):
        for i in range(5):
            self.cardList[i].__set__(otherCardList[i])

    # determine which hand is better, using the priority list in the problem
    def __lt__(self, other):
        pass

    def __str__(self):
        string = ''
        for i in range(5):
            string += self.cardList[i].__str__() + " ; "
        return string

    def high_card(self):
        self.temp_high_card = Card()
        self.temp_high_card.value = 0
        for i in range(5):
            if int(self.temp_high_card.value) < int(self.cardList[i].value):
                self.temp_high_card = self.cardList[i]

        return self.temp_high_card

    # in no particular order
    # all same suit
    def is_flush(self):
        self.temp_card = Card()
        self.temp_card = self.cardList[0]
        for i in range(5):
            if self.cardList[i].suit != self.temp_card.suit:
                return False
        return True

    # all consecutive values
    def is_straight(self):
        # CHECKME: only sorts on value alone
        sorted_cardList = sorted(self.cardList, key=operator.attrgetter('int_value'))
        first_card = Card()
        first_card = sorted_cardList[0]
        for card in sorted_cardList[1:]:
            if first_card.int_value == (card.int_value - 1):
                first_card = card
            else:
                return False
        return True

    # consecutive values and same suit
    def is_straight_flush(self):
        pass

    def is_royal_flush(self):
        pass

    def num_pairs(self):
        pass

    def has_four_of_a_kind(self):
        pass

    def has_three_of_a_kind(self):
        pass

    def compare_hands(self, otherHand):
        # A. High Card: Highest value card.
        # B. One Pair: Two cards of the same value.
        # C. Two Pairs: Two different pairs.
        # D. Three of a Kind: Three cards of the same value.
        # E. Straight: All cards are consecutive values.
        # F. Flush: All cards of the same suit.
        # G. Full House: Three of a kind and a pair.
        # H. Four of a Kind: Four cards of the same value.
        # I. Straight Flush: All cards are consecutive values of same suit.
        # J. Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

        # return 0 if we are the losing hand
        # return 1 if we are the winning hand
        print self.high_card()
        print otherHand.high_card()

        pass

player1_hands = []
player2_hands = []

def read_hands():
    #text_file = open("p054_poker.txt", "r")
    text_file = open("ptest.txt", "r")
    lines  = text_file.read().split('\n')
    for line in lines:
        if line != '':
            cards  =  re.findall(r"\b[\w]*", line)
            # filter out empty elements
            cards[:] = [item for item in cards if item != '']
            player1_hands.append(tuple(cards[0:5]))
            player2_hands.append(tuple(cards[5:10]))

def main(argv):
    #total_hands = 1000
    total_hands = 6

    read_hands()  # read in text file in to tuples

    # to preserve order of the text file containing all hands
    player1_hands.reverse()
    player2_hands.reverse()

    for currentRound in range(total_hands):

        print "Round " + str(currentRound+ 1 ) + " !! "

        # player 1
        cardTupList1 = list(player1_hands.pop())
        newCardList1 = [Card() for i in range(5)]

        for i in range(5):
            newCardList1[i].set_value(cardTupList1[i][0])
            newCardList1[i].set_suit(cardTupList1[i][1])

        print "smethin"
        Hand1 = Hand()
        Hand1.set_hand(newCardList1)
        print Hand1.__str__()
        print Hand1.high_card()

        # player 2
        cardTupList2 = list(player2_hands.pop())
        newCardList2 = [Card() for i in range(5)]

        for i in range(5):
            newCardList2[i].set_value(cardTupList2[i][0])
            newCardList2[i].set_suit(cardTupList2[i][1])

        Hand2 = Hand()
        Hand2.set_hand(newCardList2)
        print Hand2.__str__()
        print Hand2.high_card()

        # compare hands
        print "Is straight?" + str(Hand2.is_straight())

        # keep track of wins

if __name__ == "__main__":
    main(sys.argv)

# issues
# issue when txt while is 2
