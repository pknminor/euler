
import sys
import itertools
from time import time

'''
Notes:


'''
# reverse number
def reverse(num):
    temp=num
    reversed=0
    if temp == 0:
        return temp
    while(temp>0):
        reversed=reversed*10 + temp%10
        temp/=10
    return reversed

def is_palin(num):
    return reverse(num) == num

def largest_n_digit_number(n):
    num_digits = n
    largest_number = 0
    for i in range(0,num_digits):
        largest_number = largest_number + 9*(10**i)
    return largest_number

def smallest_n_digit_number(n):
    num_digits = n
    smallest_number = 0
    for i in range(0,num_digits):
        smallest_number = smallest_number + 1*(10**i)
    return smallest_number

def main(argv):
    num_digits = 3
    break_found = 0
    palin_list = []
    for i in range(largest_n_digit_number(num_digits), smallest_n_digit_number(num_digits)-1, -1):
        if break_found:
            break
        for j in range(largest_n_digit_number(num_digits), smallest_n_digit_number(num_digits)-1, -1):
            product = i * j
            if is_palin(product):
                #print "largest palin = " + str(product) + " the multiples are i = " + str(i) + " j = " + str(j)
                palin_list.append(product)
                if len(palin_list) > 10:
                #palin_found = 1
                    break
    print "PALIN LIST MAX " + str(max(palin_list))

if __name__ == "__main__":
    main(sys.argv)
