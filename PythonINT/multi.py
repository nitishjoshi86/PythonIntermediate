from multiprocessing import Process
import os
import time

def sqnum():
    for i in range(100):
        i *i
        time.sleep(0.1)
proces = []

numprocess = os.cpu_count()

#create process
for i in range(numprocess):
    p = Process(target=sqnum)
    proces.append(p)

#start
for p in proces:
    p.start()

#join
for p in proces:
    p.join()

print('end main')