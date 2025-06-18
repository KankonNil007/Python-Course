# Dictionary Methods in Python

# Update Method in Dictionary

dict1 = {
    123: 23,
    124: 45,
    128: 67,
    180: 80
    }

dict2 = {
    126: 46,
    127: 48
}

dict1.update(dict2) # adds dict2 values to dict1
print(dict1)


# Clearing all the values in a dictionary

dict2 = {
    126: 46,
    127: 48
}

dict2.clear()
print(dict2)

# Removing a certain value in a dictionary

dict1 = {
    123: 23,
    124: 45,
    128: 67,
    180: 80
    }

dict1.pop(123) # the key you wanna remove
print(dict1)


# Removing the last value in a dictionary

dict1 = {
    123: 23,
    124: 45,
    128: 67,
    180: 80
    }

dict1.popitem() # 180: 80 will be removed
print(dict1)


# Deleting out a dictionary

dict1 = {
    123: 23,
    124: 45,
    128: 67,
    180: 80
    }

del dict1
# print(dict1) # This will show an error because the dict1 was deleted

# You can also delete a certain value like pop method using del method

dict1 = {
    123: 23,
    124: 45,
    128: 67,
    180: 80
    }

del dict1[128]
print(dict1)