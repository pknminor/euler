 # Problem 51 By replacing the 1st digit of the 2-digit number *3, it turns out
 # that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all
 # prime.
 # 
 # By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
 # number is the first example having seven primes among the ten generated
 # numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
 # 56993. Consequently 56003, being the first member of this family, is the
 # smallest prime with this property.
 # 
 # Find the smallest prime which, by replacing part of the number (not necessarily
 # adjacent digits) with the same digit, is part of an eight prime value family.

import sys
import itertools

from time import time

debug=1

'''
Notes:

N-digit numbers:
    replace 1 digit
        find location of replacement between(1st digit to Nth digit)
        replace and keep count of primes

    replace 2 digits
        find locations of the 1st replacement between(1st digit to Nth digit)
        find locations of the 2nd replacements between(1st digit to Nth digit)
        replace and keep count of primes

    replace N-1 digits
        find locations of the 1st replacement between(1st digit to Nth digit)
        find locations of the 2nd replacements between(1st digit to Nth digit)
        find locations of the N-1 replacements between(1st digit to Nth digit)
        replace and keep count of primes

    replace all digits together
        replace and keep count of primes

'''
## function that iterates throught all possible two to be replaced digit locations

## function to replace the locations from 0 through 9 and keep track of the number of primes found

### dbg_print_lo
def dbg_lo(str):
    if (debug>=3):
        print str
    else:
        pass

### dbg_print_hi
def dbg_hi(str):
    if (debug>=1):
        print str
    else:
        pass

## function to determine if number is prime
#def is_prime(num):
#    temp = num
#    # return if you see a even number greater than 2
#    if ((num%2) == 0) & (num > 2):
#        return 0
#    else:
#        for i in range(2,num):
#            if float(num%i) == 0:
#                return 0
#        return 1

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


## function to return number of digits
def num_digits(num):
    temp = num
    digits = 0
    while(temp>0):
       digits += 1
       temp = temp / 10
    return digits

## function to get a new number with a digit replaced in location
## 199, 2, 8: would return 189
## 678, 3, 1: would return 671
def digit_replace(num, location, new_digit):
    temp = num
    tot_digits = num_digits(num)
    curr_digits = tot_digits
    new_num = 0
    for curr_digit_location in range(1, tot_digits+1):
        string = " curr_digit_location = " + str(curr_digit_location)
        dbg_lo(string)

        new_num *= 10

        if (tot_digits-curr_digit_location+1) == location:
            new_num += new_digit
        else:
            new_num += temp % 10
        temp /= 10

    # return reversed
    string = " num                   " + str(num)
    string += " location              " + str(location)
    string += " digit_replace output  " + str(new_num)[::-1]
    dbg_lo(string)

    return int(str(new_num)[::-1])

## function to get the prime family count given the number and the digit locations that will be replaced
def family_count(num, digit_locations):
    string =  " The original number is " + str(num)
    dbg_lo(string)

    # replace marked locations with 0-9
    prime_count = 0
    new_digit = 0

    for new_digit in range(0,9+1):
        # IMPROVEME
        string = " The new digit is " + str(new_digit)
        dbg_lo(string)

        # substitute all necessary digit locations
        newnum = num
        for location in digit_locations:
            newnum = digit_replace(newnum, location, new_digit)

        string = " The new number with replaced digit(s) is " + str(newnum)
        dbg_lo(string)

        # check if newnum is prime
        if (is_prime(newnum)) & (num_digits(newnum) == num_digits(num)):
            prime_count += 1
            string = " The new number is " + str(newnum) + "prime"
            dbg_lo(string)

        # print the prime count
        string = " The prime count is" + str(prime_count)
        dbg_lo(string)

    # make sure return are good!
    return prime_count

def step_over():
    #a = raw_input('Waiting for any key before proceeding')
    pass

# main loop
def prob_51():
    #for curr_num in range(100): #range(10000, 99999):#
    #for curr_num in range(10000, 99999):#
    #for curr_num in range(55999, 56010):#
    #for curr_num in range(10, 9999999):#
    #for curr_num in range(121300, 121413):#
    #for curr_num in range(120000, 121413):#
    for curr_num in range(100, 121413):#

        curr_num_tot_digits = num_digits(curr_num)

        if (curr_num_tot_digits > 9):
            exit()

        for num_digit_changes in range(1, curr_num_tot_digits+1):
            # create list to get various combinations of digit replaces
            # 123 1234567 12345678
            comb_input = []
            for b in range(1, curr_num_tot_digits+1):
                comb_input.append(b)

            string = "curr_num = " + str(curr_num) + " comb_input = " + str(list(comb_input))
            dbg_lo(string)

            digit_locations = list(itertools.combinations(comb_input, num_digit_changes))
            string = "curr_num = " + str(curr_num) + " digit locations = " + str(digit_locations)
            dbg_lo(string)

            step_over()
            for curr_digit_locations in digit_locations:

                string = "curr_num = " + str(curr_num) + " curr digit locations = " + str(curr_digit_locations)
                dbg_lo(string)
                step_over()

                prime_count = family_count(curr_num, curr_digit_locations)
                string = "Prime count = " + str(prime_count)
                dbg_lo(string)
                step_over()

                if (prime_count == 8):
                    string = "Found a family of 8 raccoons!! = " + str(curr_num)
                    dbg_hi(string)
                    a = raw_input('Waiting for any key before proceeding')


def main(argv):
    # main
    prob_51()
    pass

if __name__ == "__main__":
    main(sys.argv)

# test code

#num = 1334
#comb_input = []

# test num_digits
# num  = 190

# test digit_replace
# num = 56003
# location = 5
# new_digit = 4
# newnum =  digit_replace( num, location, new_digit)

# test digit_replace
# num = 566777
# location = 2
# new_digit = 4
# newnum =  digit_replace( num, location, new_digit)

# test family_count
# num = 56003
# location = 3,4
# locations = [3,4]
# family_count(56003, locations)

# test family_count
# num = 13
# location = 1
# locations = [3,4]
# family_count(56003, locations)
