# Sets in Python

set1 = {2, 4, 6, 7, 6} # Don't accept repeated values
print(set1)

# Accepts multiple data types

set2 = {"Kankon", 8, True, 5.9}
print(set2) # Sets doesn't maintain order

# Creating an Empty Set

set3 = set()
print(type(set3))

# Accessing the values using Loop

set4 = {"Kankon", 8, True, 5.9, False}
for i in set4:
    print(i)