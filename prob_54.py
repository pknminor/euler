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
# -------|-----------------------------------------------------------|--------------------------------------------------------|-------------------|---
# Hand   |     Player 1                                              |     Player 2                                           |        Winner     |
# -------|-----------------------------------------------------------|--------------------------------------------------------|-------------------|---
# 1      |     5H 5C 6S 7S KD Pair of Fives                          |    2C 3S 8S 8D TD Pair of Eights                       |        Player 2   |
# 2      |     5D 8C 9S JS AC Highest card Ace                       |    2C 5C 7D 8S QH Highest card Queen                   |        Player 1   |
# 3      |     2D 9C AS AH AC Three Aces                             |    3D 6D 7D TD QD Flush  with Diamonds                 |        Player 2   |
# 4      |     4D 6S 9H QH QC Pair of Queens    (Highest card Nine)  |    3D 6D 7H QD QS Pair of Queens (Highest card Seven)  |        Player 1   |
# 5      |     2H 2D 4C 4D 4S Full House        (With Three Fours)   |    3C 3D 3S 9S 9D Full House (with Three Threes)       |        Player 1   |
# -------|-----------------------------------------------------------|--------------------------------------------------------|-------------------|---

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
import sys, re

player1_hands = []
player2_hands = []

def read_hands():
    text_file = open("p054_poker.txt", "r")
    lines  = text_file.read().split('\n')
    for line in lines:
        if line != '':
            cards  =  re.findall(r"\b[\w]*", line)
            # filter out empty elements
            cards[:] = [item for item in cards if item != '']
            player1_hands.append(tuple(cards[0:5]))
            player2_hands.append(tuple(cards[5:10]))

def main(argv):
    read_hands()
    player1_hands.reverse()
    player2_hands.reverse()
    print player1_hands.pop()
    print player2_hands.pop()
    pass

if __name__ == "__main__":
    main(sys.argv)
