# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?


import sys
import itertools
from time import time

'''
Notes:


'''

## is_prime from the internet
## https://zach.se/project-euler-solutions/51/
def primes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=list(range(3,n+1,2))
    mroot = n ** 0.5
    half=(n+1)//2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)//2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

from bisect import bisect_left
# sqrt(1000000000) = 31622
__primes = primes(31622)
def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

def main(argv):
    # number = 13195
    number =  600851475143
    new_number = number
    factors_list = []
    # assumes number is not even
    curr_factor = 3 # only odd numbers?
    while (new_number > 1):
        if (new_number%curr_factor) == 0:
            factors_list.append(curr_factor)
            new_number = new_number / curr_factor
        else:
            curr_factor += 2

    print " printing all prime factors "
    for i in factors_list:
        if is_prime(i):
            print " prime factor = " + str(i)

if __name__ == "__main__":
    main(sys.argv)
