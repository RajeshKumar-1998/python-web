#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rajesh
#
# Created:     24-12-2019
# Copyright:   (c) Rajesh 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import threading
import time

def fun():
    time.sleep(3)
    print("fin")
def func():
    print ("hi")
    mine =  fun()
    return

def main():
    my = threading.Thread(target = func)
    time.sleep(10)
    return

if __name__ == '__main__':
    main()
