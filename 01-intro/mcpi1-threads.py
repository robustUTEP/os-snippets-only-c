#! /usr/bin/env python3
import random, time, sys

numIters = int(sys.argv[1])    
numHits = 0

startTime = time.time()
for i in range(numIters):
    random.seed(time.time())
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    if (x*x + y*y) < 1:
        numHits += 1
endTime = time.time()


print(4.0 * numHits/(float(numIters)), endTime - startTime )
