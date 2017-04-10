#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul
from random import randint

'''
Notes:

'''

dict = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'sixty',
    '80' : 'eighty',
    '90' : 'ninty',
    '100' : 'hundred',
    '1000' : 'thousand'
}

def count_string(string):
    pass

def get_answer():
    for i in range(30):
        final_string = ''
        temp_num = i
        if True: # if i in dictionary directly use that as final string
            pass
        while (temp_num): # if i not in dictionary, need to use a combinational of dictionary results and add 'and' where necessary
            if (temp_num < 10):
                pass
            if (temp_num < 100) and (temp_num > 10):
                pass
            if (temp_num < 1000) and (temp_num > 100):
                pass
        pass



def main(argv):
    get_answer()

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
