# Multithreading in Python

import threading
import time

def func1(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter() # For measuring time
# Normally running functions
func1(4)
func1(2)
func1(1)
time2 = time.perf_counter()
print(time2 - time1)

time3 = time.perf_counter()
# Parallel running functions
t1 = threading.Thread(target=func1, args=[4])
t2 = threading.Thread(target=func1, args=[2])
t3 = threading.Thread(target=func1, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time4 = time.perf_counter()
print(time4 - time3)