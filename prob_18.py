#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul
from random import randint

'''
Notes:
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
------------------------
3
7 4
2 4 6
8 5 9 3
------------------------
That is, 3 + 7 + 4 + 9 = 23.
------------------------
Find the maximum total from top to bottom of the triangle below:
------------------------
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
------------------------
    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
------------------------
'''
graph1 = []
graph1.append([3])
graph1.append([7, 4])
graph1.append([2, 4, 6])
graph1.append([8, 5, 9, 3])

graph2 = []
graph2.append([75])
graph2.append([95, 64])
graph2.append([17, 47, 82])
graph2.append([18, 35, 87, 10])
graph2.append([20, 04, 82, 47, 65])
graph2.append([19, 01, 23, 75, 03, 34])
graph2.append([88, 02, 77, 73, 07, 63, 67])
graph2.append([99, 65, 04, 28, 06, 16, 70, 92])
graph2.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
graph2.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
graph2.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
graph2.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
graph2.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
graph2.append([63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
graph2.append([04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23])

    # to traverse the tree from top down, at each node you can choose the left child or the right child, assuming the left child can be represented as 0, and the right child as 1, there are 2^n paths for a graph of depth n
    # 0000(innermost) -- 1111(outermost)
def get_max_path_sum(graph):
    num_rows = len(graph)
    all_paths_bin_dec = []
    all_paths = []

    # create binary encoded paths, where 0 represents traversing left and 1 represents traversing right down the list
    for i in range(pow((num_rows-1),2)):
        format_str = '0' + str(num_rows -1) + 'b'
        all_paths_bin_dec.append(format(i, format_str))

    # create paths list
    curr_col = 0
    max_sum = 0
    for bin_decisions in all_paths_bin_dec:
        new_path = []
        new_path.append(0)
        curr_col = 0
        sum_path = 0
        for slice_idx in range(3):
            new_path.append(curr_col + int(bin_decisions[slice_idx]))
            curr_col += int(bin_decisions[slice_idx])
        sum_path = get_sum_of_path(graph, new_path)
        if (sum_path > max_sum):
            max_sum = sum_path
        all_paths.append(new_path)

    # print max
    print "Max sum = " + str(max_sum)
    # print all_paths

# path defined as a list of col indices from the top of the tree to root in [col1, col2, col3, col4]
def get_sum_of_path(graph, path):
    sum = 0
    for i in range (0,len(graph)):
        sum += graph[i][path[i]]
        print graph[i][path[i]]
    return sum

def brute_force():
     get_max_path_sum(graph1)
    # test get sum path outermost path
    # path = [0, 1, 2, 3]
    # get_sum_of_path(path)

def get_answer():
    brute_force()

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
