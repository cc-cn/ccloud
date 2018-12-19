import numpy as np
import sys
import time
#sys.path.append("/home/deepglint/Documents/py-faster-rcnn/lib/")
#from utils.timer import Timer

#Timer.tic()
sum=10
begin=time.time()
for i in range(100000000):
        sum+=i
        sum-=i
#Timer.toc()
end=time.time()

print(end-begin)
print(sum)

