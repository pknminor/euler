#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul

'''
Notes:
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

def remove_duplicates(pre_list):
    clean_list = []
    for i in pre_list:
        if i not in clean_list:
            clean_list.append(i)
    return clean_list

def get_num_divisors_floor(num):
    prime_list = [2, 3, 5, 7, 11]
    divisor_list = []
    divisor_list.append(1)
    for curr_prime in prime_list:
        if( num % curr_prime) == 0:
                break_flag = 0
                while True:
                    #improve
                    for idx in range(num+1,num/2,-1):
                        if (idx * curr_prime) == num:
                            divisor_list.append(idx)
                            divisor_list.append(curr_prime)

    divisor_list = remove_duplicates(divisor_list)
    return len(divisor_list)

def get_num_divisors(num):
    temp_num = num
    divisor_list = []
    for idx1 in range(1,num+1):
        for idx2 in range(idx1,num+1):
            if (idx1*idx2) == num:
                divisor_list.append(idx1)
                divisor_list.append(idx2)

    divisor_list = remove_duplicates(divisor_list)
    print divisor_list
    return len(divisor_list)

def main(argv):
    got_result = 0
    new_triangle_number = 0
    iterator = 1
    break_flag = 0
    #while (got_result == 0):
    while True:
        new_triangle_number += iterator
        iterator += 1
        print " Triangle number = " + str(new_triangle_number)
        print " Iterator number = " + str(iterator)
        if iterator == 1000: # rough estimate
            print " RESULT = " + str(get_num_divisors_floor(new_triangle_number))
            break_flag = 1
            # break

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
