#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul
from random import randint

'''
sum of non abundudants under
'''
def get_sum_proper_divisors(num):
    div_sum = 0
    for i in range(1,num):
        if (num%i == 0):
            div_sum += i
    return div_sum

proper_divisors_sums = {}
def gen_proper_divisors(num):
    for i in range(1, num):
        proper_divisors_sums[i] = get_sum_proper_divisors(i)

def lookup_proper_divisors_sum(num):
    if (proper_divisors_sums[num] != ''):
        return proper_divisors_sums[num]
    else:
        print "Error: out of bounds"

def is_num_abundant(num):
    if (lookup_proper_divisors_sum(num) > num):
        return 1
    else:
        return 0

def is_sum_of_two_abundants(num):
    for i in range(1, num):
        if (is_num_abundant(i)):
            for j in range (i, num):
                if (is_num_abundant(j) & ((i+j) == num)):
                    print "evaluating num " + str(num) + " 1st " + str(i) + " 2nd " + str(j)
                    return 1
    return 0

def main(argv):
    # max_num = 30
    max_num = 28123
    gen_proper_divisors(max_num)
    sum_non_abun = 0
    for i in range(max_num):
        if is_sum_of_two_abundants(i) == 0:
            sum_non_abun += i
    print sum_non_abun

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
