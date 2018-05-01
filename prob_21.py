#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul
from random import randint

'''
sum of amicable
'''

def get_sum_proper_divisors(num):
    div_sum = 0
    for i in range(1,num):
        if (num%i == 0):
            div_sum += i
    return div_sum

def get_amicable_under(num):
    sum_of_divisors_dict = {}
    sum_of_amicable_under = 0
    for i in range(1,num):
        sum_of_divisors_dict[i] = get_sum_proper_divisors(i)
    for j in range(1,num):
        for k in range(1,num):
            if (sum_of_divisors_dict[j] == k) & (j == sum_of_divisors_dict[k]) & (j != k):
                # print "1st " + str(j) + " 2nd " + str(k)
                sum_of_amicable_under += j
    return sum_of_amicable_under

def main(argv):
    print get_amicable_under(10000)

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
