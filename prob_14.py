#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul

'''
Notes:

'''
def get_next_num(num):
    new_num = num
    if num == 0:
        print "get_next_num: new_num = 0"
        sys.exit()
    elif (num%2) == 0:
        new_num /= 2
    elif (num%2) != 0:
        new_num = (3*num) + 1
    # print "new_num" + str(new_num)
    return new_num

def get_seqLength(num):
    seqLength = 1
    new_num = num
    while(new_num != 1):
        new_num = get_next_num(new_num)
        seqLength +=1
    # print "num" + str(num)
    # print "seqLength" + str(seqLength)
    return seqLength

def main(argv):
    ITER_MAX = 1000000
    LEN_MAX  = 0
    LEN_MAX_START  = 0
    for i in range(3,ITER_MAX+1):
        newLength = get_seqLength(i)
        if newLength > LEN_MAX:
            LEN_MAX = newLength
            LEN_MAX_START = i
    print "LEN_MAX = " + str(LEN_MAX)
    print "LEN_MAX_START = " + str(LEN_MAX_START)

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
