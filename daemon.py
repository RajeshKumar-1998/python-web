#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rajesh
#
# Created:     31-12-2019
# Copyright:   (c) Rajesh 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import threading
import time
import logging

def daemon():
    logging.DEBUG('Starting')
    time.sleep(0.5)
    logging.DEBUG('Exiting')
    return

def non_daemon():
    logging.DEBUG('Starting')
    logging.DEBUG('Exiting')
    return


def main():

    logging.basicConfig( level = logging.DEBUG, format = '(%(threadName)-10s) %(message)s',)

    d= threading.Thread(name = daemon, target = daemon ,daemon =True)

    t= threading.Thread(name=non_daemon, target = non_daemon)

    d.start()

    t.start()

    if __name__ == '__main__':

        main()
