import threading
import time

global_var = 0

def ThreadProc() : 
    global global_var
    for iter in range(1000000) : 
        global_var += 1

hThread1 = threading.Thread(target=ThreadProc)
hThread2 = threading.Thread(target=ThreadProc)
hThread3 = threading.Thread(target=ThreadProc)

hThread1.start()
hThread2.start()
hThread3.start()

hThread1.join()
hThread2.join()
hThread3.join()

# you should notice that this is the type of unsafe multithreading
# when more than one thread tends to write into one global variable
print(global_var)