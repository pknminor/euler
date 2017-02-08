import sys
import itertools
import timeit
import elib
from operator import mul

'''
Notes:


'''

# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def product_phiar(phiar):
    phiar_product = 1
    for i in phiar:
        phiar_product *= i
    return phiar_product

def find_greatest_product(matrix):
    tot_matrix_rows = len(matrix)
    tot_matrix_cols = len(matrix[0])

    greatest_phiar_product = 0
    greatest_phiar = []

    # traverse matrix horizontally looking for largest product
    starting_col_index_first = 0
    starting_col_index_last = tot_matrix_cols - 3 #  4 - 1 

    for row in range(0,tot_matrix_rows):
        for idx in range(starting_col_index_first,starting_col_index_last):
            phiar = []
            phiar.append(matrix[row][idx])
            phiar.append(matrix[row][idx+1])
            phiar.append(matrix[row][idx+2])
            phiar.append(matrix[row][idx+3])

            phiar_product = product_phiar(phiar)

            print " PHIAR HORIZONTAL = " + str(phiar)

            if (phiar_product > greatest_phiar_product):
                greatest_phiar_product = phiar_product
                greatest_phiar = phiar


    # traverse matrix vertically looking for largest product
    starting_row_index_first = 0
    starting_row_index_last = tot_matrix_rows - 3 #  4 - 1 
    for col in range(0,tot_matrix_cols):
        for idx in range(starting_row_index_first,starting_row_index_last):
            phiar = []
            phiar.append(matrix[idx][col])
            phiar.append(matrix[idx+1][col])
            phiar.append(matrix[idx+2][col])
            phiar.append(matrix[idx+3][col])

            phiar_product = product_phiar(phiar)

            print " PHIAR VERTICAL = " + str(phiar)

            if (phiar_product > greatest_phiar_product):
                greatest_phiar_product = phiar_product
                greatest_phiar = phiar

    # traverse diagonally forward slash
    starting_col_index_first = 3
    starting_col_index_last = tot_matrix_cols
    for row in range(0,tot_matrix_rows-3):
        for idx in range(starting_col_index_first,starting_col_index_last):
            phiar = []
            phiar.append(matrix[row][idx])
            phiar.append(matrix[row+1][idx-1])
            phiar.append(matrix[row+2][idx-2])
            phiar.append(matrix[row+3][idx-3])

            phiar_product = product_phiar(phiar)

            print " PHIAR DIAGONAL FORWARD = " + str(phiar)

            if (phiar_product > greatest_phiar_product):
                greatest_phiar_product = phiar_product
                greatest_phiar = phiar


    # traverse diagonally back slash 
    starting_row_index_first = 0
    starting_row_index_last = tot_matrix_rows - 3 #  4 - 1 
    for col in range(0,tot_matrix_cols-3):
        for idx in range(starting_row_index_first,starting_row_index_last):
            phiar = []
            phiar.append(matrix[idx][col])
            phiar.append(matrix[idx+1][col+1])
            phiar.append(matrix[idx+2][col+2])
            phiar.append(matrix[idx+3][col+3])

            phiar_product = product_phiar(phiar)

            print " PHIAR DIAGONAL BACKWARD = " + str(phiar)

            if (phiar_product > greatest_phiar_product):
                greatest_phiar_product = phiar_product
                greatest_phiar = phiar

    print " GREATEST PHIAR = " + str(greatest_phiar)
    print " GREATEST PHIAR PRODUCT = " + str(greatest_phiar_product)


def main(argv):
    matrix = []
    matrix.append([8, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91, 8])
    matrix.append([49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00])
    matrix.append([81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65])
    matrix.append([52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91])
    matrix.append([22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80])
    matrix.append([24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50])
    matrix.append([32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70])
    matrix.append([67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21])
    matrix.append([24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72])
    matrix.append([21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95])
    matrix.append([78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14, 9, 53, 56, 92])
    matrix.append([16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57])
    matrix.append([86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58])
    matrix.append([19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40])
    matrix.append([04, 52, 8, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66])
    matrix.append([88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69])
    matrix.append([04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36])
    matrix.append([20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16])
    matrix.append([20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54])
    matrix.append([01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 01, 89, 19, 67, 48])
    find_greatest_product(matrix)

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
