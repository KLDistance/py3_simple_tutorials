import threading
import time
from queue import Queue
import random

# this is a simple instance of primitive producer-consumer model

# create consumer trigger
hEvent = threading.Event()
# global pipe
pipe = Queue()

def Producer() : 
    counter = 0
    while counter < 10 : 
        rm = random.uniform(0, 100)
        pipe.put(rm)
        hEvent.set()
        print('producer makes: ', rm)
        counter += 1
        time.sleep(0.5)

def Consumer() : 
    counter = 0
    while counter < 10 : 
        if pipe.empty() : 
            hEvent.wait()
            hEvent.clear()
        print('consumer gets: ', pipe.get())
        counter += 1

hThread1 = threading.Thread(target=Producer)
hThread2 = threading.Thread(target=Consumer)
hThread1.start()
hThread2.start()
hThread1.join()
hThread2.join()