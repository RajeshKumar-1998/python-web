#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rajesh
#
# Created:     25-12-2019
# Copyright:   (c) Rajesh 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
from threading import Thread
import time

def addto(a,b):
    chars = a+b
    return addto(a,b)

def main():
    addto(5,2)
    """ tm = time.localtime()
    print("wait for few sec")
    time.sleep(5)
    print (tm)  """
    print(addto(5,2))

if __name__ == '__main__':
    main()
