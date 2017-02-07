# The sum of the squares of the first ten natural numbers is,
# 
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import sys
import itertools
from time import time

'''
Notes:


'''
def sum_of_numbers_till(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

def sqr(num):
    return (num ** 2)

def sqr_of_sum(num):
    return sqr(sum_of_numbers_till(num))

def sum_of_sqrs(num):
    sum_of_sqrs = 0
    for i in range(1,num+1):
        sum_of_sqrs += sqr(i)
    return sum_of_sqrs

def sum_diff(num):
    return (sqr_of_sum(num) - sum_of_sqrs(num))

def main(argv):
    diff = sum_diff(100)
    print " ANS = " + str(diff)

if __name__ == "__main__":
    main(sys.argv)

