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
#!/usr/bin/python

### This func returns the number of threads currently in execution
## Let us modify the last script thread fn

import os
import threading
import time
from threading import Thread

def Treadfn(i):
    print("thread %i is going to to sleep for 5 sec"% i)
    time.sleep(5)
    print("Threads %i is awake now"% i)


def main():
    for i in range(10):
        mythread = Thread(target = Treadfn,args=(i, ))
        mythread.start()
        print("Current Threading Count %i" % threading.active_count())



if __name__ == '__main__':
    main()
