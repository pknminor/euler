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
def get_next_indice(curr_w, curr_h, end_w, end_h):
    ret_w, ret_h = curr_w, curr_h
    new_direction = randint(0,1)
    # print "new_direction" + str(new_direction)
    if curr_w == end_w:
        ret_h +=1
    elif curr_h == end_h:
        ret_w +=1
    elif new_direction:
        ret_w += 1
    else:
        ret_h += 1
    # print "returning w = " + str(ret_w) + " h = " + str(ret_h)
    return ret_w, ret_h

def get_num_paths():
    total_paths = 0
    start_w, start_h = 0, 0
    # end_w, end_h = 2, 2
    end_w, end_h = 20, 20
    Matrix = [[0 for x in range(end_w)] for y in range(end_h)]

    Paths = []
    repeat_counter = 0
    break_flag = 0

    while 1:
        if break_flag:
            break

        curr_w, curr_h = start_w, start_h
        currPath = []
        currPath.append([0, 0])

        while (curr_w < end_w) or (curr_h < end_h):
            curr_w, curr_h = get_next_indice(curr_w, curr_h, end_w, end_h)
            currPath.append([curr_w, curr_h])

        # check if this is a unique path
        if currPath not in Paths:
            # append path to list
            Paths.append(currPath)
        else:
            if repeat_counter < 100:
                repeat_counter += 1
                print "Paths" + str(Paths) + "repeat counter" + str(repeat_counter)
            else:
                print "Paths" + str(Paths) + "repeat counter" + str(repeat_counter) + ", stop searching for new paths"
                break_flag = 1

    numPaths = len(Paths)

    # print "Paths" + str(Paths)
    print "Num Paths" + str(len(Paths))

def main(argv):
    get_num_paths()

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
