###############################################################################################################################################~
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce palindromes so quickly. For example,
# 
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
# That is, 349 took three iterations to arrive at a palindrome.  Although no
# one has proved it yet, it is thought that some numbers, like 196, never
# produce a palindrome. A number that never forms a palindrome through the
# reverse and add process is called a Lychrel number. Due to the theoretical
# nature of these numbers, and for the purpose of this problem, we shall assume
# that a number is Lychrel until proven otherwise. In addition you are given
# that for every number below ten-thousand, it will either (i) become a
# palindrome in less than fifty iterations, or, (ii) no one, with all the
# computing power that exists, has managed so far to map it to a palindrome. In
# fact, 10677 is the first number to be shown to require over fifty iterations
# before producing a palindrome: 4668731596684224866951378664 (53 iterations,
# 28-digits).  Surprisingly, there are palindromic numbers that are themselves
# Lychrel numbers; the first example is 4994.  How many Lychrel numbers are
# there below ten-thousand?  NOTE: Wording was modified slightly on 24 April
# 2007 to emphasise the theoretical nature of Lychrel numbers.
###############################################################################################################################################~
# Solution: brute force method seems simple enough, iteratively check, reverse and add
## function to check if number if lychrel or not

import sys
from time import time

# reverse number
def reverse(num):
    temp=num
    reversed=0
    if temp == 0:
        return temp
    while(temp>0):
        reversed=reversed*10 + temp%10
        temp/=10
    return reversed

# check if palindrome
def is_palin(num):
    return reverse(num) == num

# check if lycheral within 50 iterations
def is_lychrel(num):
    iter=0
    newnum = num
    print "num = " + str(num)
    while True:
        newnum += reverse(newnum)
        print "newnum = " + str(newnum) + " iteration count = " + str(iter)
        if is_palin(newnum):
            print "It took " + str(iter) + " iterations to get a palindrome"
            return True
        if iter > 50:
            print "Found a lycheral number = " + str(num)
            return False
        else:
            iter+=1

def main(argv):
    num_not_lycheral=0
    for i in range(10000):
        if is_lychrel(i) == False:
            num_not_lycheral+=1
    print "Total num" + str(num_not_lycheral)

if __name__ == "__main__":
    main(sys.argv)
