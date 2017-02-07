# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys
import itertools
from time import time

'''
Notes:


'''
def is_divisible_by_all_till(num_of_nums, num):
    for i in range(2, num_of_nums+1):
        if (num%i != 0):
            print " Number not divisible by i = " + str(i)
            return 0
    return 1

def main(argv):
    num_of_nums = 20
    product_of_all = 1
    product_of_all_primes = 1
    product_of_all_reduced = 1
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19]
    prod_list_reduced = [11, 3, 2, 2, 13, 7, 2, 3, 5, 2, 2, 2, 2, 17, 18, 19, 20]
    for i in range(1, num_of_nums+1):
        product_of_all *= i

    for i in prime_list:
        product_of_all_primes *= i

    for i in prod_list_reduced:
        product_of_all_reduced *= i

    print " prod = " + str(product_of_all)
    print " prod reduced = " + str(product_of_all_reduced)
    print " prod prime  = " + str(product_of_all_primes)

    minimum = product_of_all_primes
    maximum = product_of_all_reduced

    product_of_all_primes *= 2
    product_of_all_primes *= 2
    product_of_all_primes *= 3
    product_of_all_primes *= 2
    minimum = product_of_all_primes
    maximum = product_of_all_primes
    for i in range(minimum, maximum+1):
        if is_divisible_by_all_till(num_of_nums, i):
            print " ANS = " + str(i)
            break

if __name__ == "__main__":
    main(sys.argv)
