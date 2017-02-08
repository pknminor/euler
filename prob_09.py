# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import sys
import itertools
from time import time
import timeit

'''
Notes:

Added timeit wrapper function and call for timing functions


'''
# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def main(argv):
    a = b = c = 0
    break_free = 0
    for a in range(1,1000):
        if break_free:
            break
        for b in range(1,1000):
            if break_free:
                break
            for c in range(1,1000):
                if break_free:
                    break
                if ((a<b) and (b<c) and ( (a ** 2) + (b ** 2) == (c ** 2) ) and ((a + b + c) == 1000)):
                    print str(a) + " " + str(b) + " " + str(c)
                    print "ANS = " + str(a * b * c)
                    break_free = 1

if __name__ == "__main__":
    #main(sys.argv)
    wrapped = wrapper(main, sys.argv)
    print str(timeit.timeit(wrapped, number=1)) + "secs"
