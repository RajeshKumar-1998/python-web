#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Rajesh
#
# Created:     28-12-2019
# Copyright:   (c) Rajesh 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Progrom from python to illustarte the Thread Concepts
#Now we going to get process id
import os
from threading import Thread
import sys
import time

def task1():
    print("Task 1 assigned to first thread:{}".format(threading.current_thread().name))
    print("Task 1 thread pid should be shown as follows {}".format(os.getpid()))
    print("Task 1 thread parent process id shown as follows {}".format(os.getppid()))

def task2():
    print("Task 2 assigned to second thread:{}".format(threading.current_thread().name))
    print("Task 2 thread pid shown as follows: {}".format(os.getpid()))
    print("Task 2 thread parent process id should be shown as follows {}".format(os.getppid()))

def main():
    #print ID of current process
    print("Get id of process running main program {}".format(os.getpid()))

    #print name of main thread
    print("Get main thread name {}".format.main_thread().name)

    #creating threads

    t1 = threading.Thread(target= task1,name ='t1')
    t2 = threading.Thread(target = task2,name ='t2')

    #start threads
    t1.start()
    t2.start()

    #wait thread for untill process
    t1.join()
    t2.join()

    if __name__ == '__main__':
        main()
