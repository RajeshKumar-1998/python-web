#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rajesh
#
# Created:     26-12-2019
# Copyright:   (c) Rajesh 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
from threading import Thread
import threading
import time

def cal(a,b):
    # this is a user dfd fn
    print("Given numbers = %s %s "%a %b)
    print("Result %d"  %int(a +b))
    return

def main():
    my=threading.Thread(target = cal, args = (14,15))
    my.start()

if __name__ == '__main__':
    main()
