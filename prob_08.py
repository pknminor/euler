import sys
import itertools
from time import time

'''
Notes:

'''

'''
7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
'''
really_long_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

def convert_number_to_list(num):
    number_list = []
    temp_num = num
    while (temp_num > 0):
        number_list.append(temp_num%10)
        temp_num /= 10
    print " total num of elements " + str(len(number_list))
    return number_list[::-1]
    # return number_list

def find_greatest_product(number_adjacents,number_list):
    greatest_product = 1
    for idx in range(0,len(number_list)):
        if (idx < (len(number_list) - number_adjacents)):
            current_product = 1
            for k in range(idx,idx+number_adjacents):
                    current_product = current_product * number_list[k]
                    print " cur = " + str(current_product)
        if current_product > greatest_product:
            greatest_product = current_product
    print " ANS = " + str(greatest_product)

def main(argv):
  print str(really_long_number)
  number_list = convert_number_to_list(really_long_number)

  # print "START"
  # print number_list[0]
  # print number_list[1]
  # print number_list[2]
  # print "..."
  # print number_list[-1]
  # print number_list[-2]
  # print number_list[-3]
  # print "END"

  # find_greatest_product(4,number_list)
  find_greatest_product(13,number_list)

if __name__ == "__main__":
    main(sys.argv)

