#!/bin/python

import os,time,sys

def run_file(file):
    try:
        execfile(file)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
        time.sleep(5)

while [1]:
    file = "prob_54.py"
    run_count = 0
    prev_stamp = os.stat(file)[8]
    time.sleep(1)
    new_stamp = os.stat(file)[8]
    if prev_stamp != new_stamp:
        run_count += 1
        execfile("clear.py")
        print "Change detected running..."
        print "Run count = " + str(run_count)
        time.sleep(5)
        run_file(file)
        time.sleep(20)
    else:
        execfile("clear.py")
        print "Autorun is paused..."

exit()
