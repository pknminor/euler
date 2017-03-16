#!/usr/bin/python
import sys
import itertools
import timeit
import elib
from operator import mul

# TBD improve commenting

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


# timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def main(argv):
    "This would create first object of Employee class"
    emp1 = Employee("Zara", 2000)
    "This would create second object of Employee class"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print "Total Employee %d" % Employee.empCount

if __name__ == "__main__":
    wrapped = wrapper(main, sys.argv)
    main(sys.argv)
    #print "timeit: main(sys.argv) took " + str(timeit.timeit(wrapped, number=1)) + "secs!"
