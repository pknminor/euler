import sys
import itertools
import timeit
import elib
from operator import mul
from decimal import *
from bigfloat import *

'''
Notes:
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

'''
def digital_sum(num):
    sum = sqrt(2, precision(350)) 
    print
    return sum

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def main(argv):
    print digital_sum(2)

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
