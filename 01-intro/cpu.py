#! /usr/bin/env python3

import sys, os, time

arg1 = sys.argv[1]

def delay(duration):
    start = time.time()
    end = start + duration
    while time.time() < end:
        continue

while 1:
    print(arg1)
    delay(1)

