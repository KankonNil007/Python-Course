# Time Module in Python

import time

def usingWhile():
    i = 0
    while (i < 1000):
        print(i)
        i = i + 1

def usingFor():
    for i in range(1000):
        print(i)


init = time.time() # This tells us the time which past from 1970 in seconds
usingWhile()
print(time.time() - init) # Tells us how long the while loop was running

init2 = time.time()
usingFor()
print(time.time() - init2) # Same as While loop


# Time.sleep() Function

print("Hello Guys")
time.sleep(2) # Program will wait for 2 seconds before running the after codes
print("This will be printed after 2 seconds")


# Time.strftime() Function
import time

t = time.localtime() # Takes the local machine's time

formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", t) # Decides in which order to print time

print(formatted_time) # Prints out the time in our local machine