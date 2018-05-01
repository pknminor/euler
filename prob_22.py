#!/usr/bin/python

import sys
import itertools
import timeit
import elib
from operator import mul
from random import randint
from string import ascii_lowercase

'''
name score
'''
def read_all_names_from_file(file_name):
    name_list = []
    text_file = open(file_name, "r")
    lines  = text_file.read().split(',')
    for line in lines:
        if line != '':
            string_clean = line[1:]
            string_clean = string_clean[:-1]
            name_list.append(string_clean);
    return name_list

# used to convert str to numbers for example ABC = [1, 2, 3]
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}

def get_name_worth(name):
    name = name.lower()
    numbers = [LETTERS[character] for character in name if character in LETTERS]
    numbers = [int(number) for number in numbers]
    return sum(numbers)

def get_name_score_total():
    name_score_total = 0
    name_list = read_all_names_from_file("p022_names.txt")
    name_list = sorted(name_list)
    j = 1
    name_list_rank = {}
    for i in name_list:
        name_list_rank[i] = j
        j +=1
    for i in name_list:
        name_score = get_name_worth(i) * name_list_rank[i]
        name_score_total += name_score
    return name_score_total

def main(argv):
    print get_name_score_total()

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
