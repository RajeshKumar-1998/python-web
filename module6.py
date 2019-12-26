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
import threading
from  threading import Thread
import time

def usr():
    print("Wait for few secs")
    time.sleep(5)
    mypath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(mypath)
    return

def main():
    inp = input("Enter the query")
    print(inp)
    print("Your Query is being processing !!!")
    usr()


if __name__ == '__main__':
    main()
