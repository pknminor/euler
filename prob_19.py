#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul
from random import randint

'''
'''

def get_factorial(num):
    if (num == 1):
        return num
    else:
        return (num * get_factorial(num-1))

def get_sum_of_digits(num):
    temp_num = num
    sum_of_digits = 0
    while (temp_num > 1):
        sum_of_digits += temp_num % 10
        temp_num /= 10
    return sum_of_digits

def main(argv):
    print get_sum_of_digits(get_factorial(100))

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
