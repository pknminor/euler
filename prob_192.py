# Let x be a real number.  A best approximation to x for the denominator bound d
# is a rational number r/s in reduced form, with s ((less than or equal)) d, such that any rational
# number which is closer to x than r/s has a denominator larger than d:
# |p/q-x| < |r/s-x| ((implication)) q > d For example, the best approximation to ((sqrt))13 for the
# denominator bound 20 is 18/5 and the best approximation to ((sqrt))13 for the
# denominator bound 30 is 101/28.
# Find the sum of all denominators of the best approximations to ((sqrt))n for the
# denominator bound 1012, where n is not a perfect square and 1 < n ((less than or equal to)) 100000.

import sys
import math
from time import time

#Solution:
def find_best_sqrt_approx(number, denom_bound):
    expected_sqrt = float(number**(0.5))
    closest_approx = 0
    new_diff = float("inf")
    print "expected = " + str(expected_sqrt)
    for i in range(1, denom_bound+1):
        for j in range(1, 1000):
            calc_res = float(j)/float(i)
            diff = float(expected_sqrt) - float(calc_res)
            print "calc_res = " + str(calc_res)
            print "diff = " + str(diff) + " abs_diff " + str(abs(diff))
            if (abs(diff) <= new_diff):
                new_diff = abs(diff)
                numerator = j
                denom = i
                print "approx = " + str(diff) + " num = " + str(numerator) + " denom = " + str(denom)
    return (numerator, denom)

def main(argv):
    print "Result x, y = " + str(find_best_sqrt_approx(13, 30))

if __name__ == "__main__":
    main(sys.argv)




# Notes:
# Instead of worrying of optimal solutions to bound numerator just use 10^12 for numerator and denom
# While running system reaches some memory limits due to the excessiveliy large search space
# To get output in floating precision, all inputs need to type-casted to float prior operation
# Looking at the example they seem to be looking for reduced fractions


