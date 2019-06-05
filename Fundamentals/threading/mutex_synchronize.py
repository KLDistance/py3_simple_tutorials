import threading

mutex_lock = threading.Lock()
global_var = 0

def ThreadProc() : 
    global global_var
    for iter in range(1000000) : 
        # only 1 thread goes into the critical section
        mutex_lock.acquire()
        # only 1 thread operate the global value now in this section
        global_var += 1
        # the thread goes out of critical section, leaves the lock to other threads
        mutex_lock.release()

hThread1 = threading.Thread(target=ThreadProc)
hThread2 = threading.Thread(target=ThreadProc)
hThread3 = threading.Thread(target=ThreadProc)

hThread1.start()
hThread2.start()
hThread3.start()

hThread1.join()
hThread2.join()
hThread3.join()

# the result should be 3000000 now, althrough may be much slower
# so you must have noticed that, synchronization between threads usually drag down the running speed
print(global_var)