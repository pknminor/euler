#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul
from random import randint

'''
'''
def num_digits(num):
    j = 0
    while (num):
        j += 1
        num /= 10
    return j

def find_num_digits_fib(digits_max):
    fib_index = 2
    fib_first_num = 1
    fib_second_num = 1
    temp = 1
    while (num_digits(fib_second_num) < digits_max):
        temp = fib_second_num
        fib_second_num = fib_first_num + fib_second_num
        fib_first_num = temp
        fib_index += 1
        # print "FIRST = " + str(fib_first_num)
        # print "SECOND = " + str(fib_second_num)
        # print "INDEX = " + str(fib_index)
    print "ANS = " + str(fib_index)

def main(argv):
    find_num_digits_fib(1000)

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
