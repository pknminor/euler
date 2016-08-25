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

debug=3

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

# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

## function to determine if number is prime
def is_prime(num):
    temp = num
    # return if you see a even number greater than 2
    if ((num%2) == 0) & (num > 2):
        return 0
    else:
        for i in range(2,num):
            if float(num%i) == 0:
                return 0
        return 1

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
        if (tot_digits-curr_digit_location+1) == location[0]:
            new_num += new_digit
        else:
            new_num += temp%10
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

        newnum = num
        for location in digit_locations:
            newnum = digit_replace(newnum, location, new_digit)

        string = " The new number with replaced digit is " + str(newnum)
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

# main loop
def prob_51():
    #for curr_num in range(100): #range(10000, 99999):#
    for curr_num in range(10000, 99999):#
        curr_num_tot_digits = num_digits(curr_num)
        if (curr_num_tot_digits > 9 ):
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

            prime_count = family_count(curr_num, digit_locations)
            if (prime_count == 7):
                string = "Found a family of 7 raccoons!! = " + str(curr_num)


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
