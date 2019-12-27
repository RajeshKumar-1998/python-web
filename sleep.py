#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Rajesh
#
# Created:     27-12-2019
# Copyright:   (c) Rajesh 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys,os
from threading import Thread
import time

# creating function for thread
def th(i):
    print(" %d Sleeping 2 sec from threads\n"%i)
    time.sleep(2)
    print("\n %d After from sleep from thread"%i)

def main():

    #start the thread fn
    for i in range(10):
        t1 = Thread(target = th, args = (i,))
        t1.start()
if __name__ == '__main__':
    main()
