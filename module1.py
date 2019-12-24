#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rajesh
#
# Created:     23-12-2019
# Copyright:   (c) Rajesh 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import threading
import time
import calendar

def fun():
    print (time.localtime())
    return time
def cal():
    calen = calendar.month(2019,3,2,1)
    print(calen)
    return calen

def main():
    mythread = threading.Thread(target=fun)
    mythread.start()
    th =time.sleep(5)
    cal()

if __name__ == '__main__':
    main()
