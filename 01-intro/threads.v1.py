#! /usr/bin/env python3

import sys, threading

total = 0
limit = int(sys.argv[1])
mutex = threading.Lock();

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global limit, total
        for i in range(limit):
            mutex.acquire()
            total += 1
            mutex.release()
workers = [Worker() for discard in range(2)] # create workers

for w in workers: w.start()     # start workers

for w in workers: w.join()      # wait for workers to terminate

print(total)
