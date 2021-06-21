from threading import Thread
import os
import time

""" def sqnum():
    for i in range(100):
        i *i
        time.sleep(0.1)


if __name__ == '__main__':
    threa = []    
    numthread = 10

    #create thread
    for i in range(numthread):
        p = Thread(target=sqnum)
        threa.append(p)

    #start
    for p in threa:
        p.start()

    #join
    for p in threa:
        p.join()

    print('end main') 
 """
datavalue = 0

def increase():
    global datavalue
    localcopy = datavalue

    #processing
    localcopy += 1
    time.sleep(0.1)

    datavalue = localcopy


if __name__ == '__main__':
    print('startvalue', datavalue)

    threa1 = Thread(target=increase)
    threa2 = Thread(target=increase)

    threa1.start()
    threa2.start()

    threa1.join()
    threa2.join()

    print('endvalue', datavalue)
    print('endmain')