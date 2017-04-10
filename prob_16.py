#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul
from random import randint

'''
Notes:

'''
def get_answer():
    num = pow(2, 1000)
    sum = 0
    while num:
        sum += num % 10
        num = num / 10
    print "SUM " + str(sum)

def main(argv):
    get_answer()

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
