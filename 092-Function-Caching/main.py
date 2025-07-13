# Function Caching in Python

import functools
import time

@functools.lru_cache(maxsize=None)
def myFunc(n):
    time.sleep(3)
    return f"5 X {n} = {5 * n}"

print(myFunc(5)) # Saved in Memory - Cache
print("Done For 5")
print(myFunc(8)) # Saved in Memory - Cache
print("Done For 8")
print(myFunc(9)) # Saved in Memory - Cache
print("Done For 9")

print(myFunc(5)) # Reused from Memory - Cache
print("Done For 5")
print(myFunc(8)) # Reused from Memory - Cache
print("Done For 8")

print(myFunc(77)) # Can't be reused from Memory because it is not saved in memory
print("Done For 77")