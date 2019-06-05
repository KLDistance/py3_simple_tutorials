import threading
import time

# thread process function
def ThreadProc(thread_name, upper_bound, delay) : 
    count = 0
    while count < upper_bound :
        time.sleep(delay)
        count += 1
        print(thread_name, ' ', count)

try :
    # declare the threads
    hThread1 = threading.Thread(target = ThreadProc, args=['thread1', 10, 0.5])
    hThread2 = threading.Thread(target = ThreadProc, args=['thread2', 6, 0.9])
    # start the threads
    hThread1.start()
    hThread2.start()
    # you should wait for the thread terminates naturally
    hThread1.join()
    hThread2.join()
    print('Threads exit')
except :
    print('Error : unable to create or start threads')