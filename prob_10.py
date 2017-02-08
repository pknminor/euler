import sys
import itertools
import timeit
import elib

'''
Notes:
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

Added timeit wrapper function and call for timing functions

'''

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def main(argv):
    sum_primes = 0
    for i in range(1,2000000):
        if (elib.is_prime(i)):
            sum_primes += i
    print " ANS = " + str(sum_primes)

if __name__ == "__main__":
    #main(sys.argv)
    wrapped = wrapper(main, sys.argv)
    print str(timeit.timeit(wrapped, number=1)) + "secs"



