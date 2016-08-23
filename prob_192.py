# Let x be a real number.  A best approximation to x for the denominator bound d
# is a rational number r/s in reduced form, with s ((less than or equal)) d,
# such that any rational number which is closer to x than r/s has a 
# denominator larger than d:

# |p/q-x| < |r/s-x| ((implication)) q > d

# For example, the best approximation to ((sqrt))13 for the
# denominator bound 20 is 18/5 and the best approximation to ((sqrt))13 for the
# denominator bound 30 is 101/28.

# Find the sum of all denominators of the best approximations to ((sqrt))n for the
# denominator bound 10**12, where n is not a perfect square and 1 < n ((less than or equal to)) 100000.

import sys
import math
from time import time
from fractions import gcd

#Solution:
def is_perfect_square(number):
    res_sqrt = float(number**(0.5))
    (numer, denom) = res_sqrt.as_integer_ratio()
    if (denom == 1):
        return True
    else:
        return False

def find_best_sqrt_approx(number, denom_bound):
    expected_sqrt = float(number**(0.5))
    closest_approx = 0
    new_diff = float("inf")
    #print "expected = " + str(expected_sqrt)
    for i in range(1, denom_bound+1):
        for j in range(1, 1000):
            calc_res = float(j)/float(i)
            diff = float(expected_sqrt) - float(calc_res)
            #print "calc_res = " + str(calc_res)
            #print "diff = " + str(diff) + " abs_diff " + str(abs(diff))
            if (abs(diff) <= new_diff):
                new_diff = abs(diff)
                numerator = j
                denom = i
                #print "approx = " + str(diff) + " num = " + str(numerator) + " denom = " + str(denom)

    # reduce fraction
    res_gcd = gcd(numerator, denom)
    return (numerator/res_gcd, denom/res_gcd)

def main(argv):
    #(x, y) = find_best_sqrt_approx(13, 10**2)
    #print "Result x, y = " + str(x) + " y = "+ str(y)
    print "Starting"
    #sys.exit()
    denom_sum = 0
    for i in range(1, 100000+1):
        if ( is_perfect_square(i) == False ):
            (approx_num, approx_denom) = find_best_sqrt_approx(i, 10**5)
            denom_sum += approx_denom
    print " Sum of approximated denominators = " + denom_sum

if __name__ == "__main__":
    main(sys.argv)

# Notes:
# Instead of worrying of optimal solutions to bound numerator just use 10^12 for numerator and denom
# While running system reaches some memory limits due to the excessiveliy large search space
# To get output in floating precision, all inputs need to type-casted to float prior operation


