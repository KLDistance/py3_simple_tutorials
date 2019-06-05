import threading
import time

# to design the two thread with alternating execution
hEvent1 = threading.Event()
hEvent2 = threading.Event()
global_var = 0

def ThreadProc1() : 
    global global_var
    for iter in range(100000) : 
        hEvent1.wait()
        global_var += 1
        hEvent1.clear()
        hEvent2.set()

def ThreadProc2() : 
    global global_var
    for iter in range(100000) : 
        hEvent2.wait()
        global_var += 1
        hEvent2.clear()
        hEvent1.set()

hThread1 = threading.Thread(target=ThreadProc1)
hThread2 = threading.Thread(target=ThreadProc2)

hThread1.start()
hThread2.start()

# trigger one thread to start the process
hEvent1.set()

hThread1.join()
hThread2.join()

# same effect on synchronization
print(global_var)