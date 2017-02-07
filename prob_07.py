# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

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
    num_of_primes_needed = 10001
    num_of_primes_found = 2
    prime_candidate = 3
    last_prime = 0
    while (num_of_primes_found < num_of_primes_needed):
        prime_candidate += 2
        if (is_prime(prime_candidate)):
            num_of_primes_found += 1
    last_prime = prime_candidate
    print "ANS = " + str(last_prime)

if __name__ == "__main__":
    main(sys.argv)


