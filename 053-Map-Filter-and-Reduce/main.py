# Map, Filter and Reduce Function in Python

# Map Function 

def cube(x):
    return x*x*x

list1 = [2, 4, 6, 3, 8, 7]

# If you wanna turn the list into a cubed list , you can use for loop

newList= []

for i in list1:
    newList.append(cube(i))

print(newList)

# You can also do this using map method

list3 = [2, 4, 6, 3, 8, 7, 8, 9, 4]

newList2 = list(map(cube, list3))
print(newList2)


# filter Function : enlists items on a certain condition

def condi(x):
    return x > 3

list2 = [2, 4, 8, 9, 4]
newList3 = list(filter(condi, list2))
print(newList3)


# We can use lambda functions instead of regular functions

list5 = [3, 4, 2, 7, 9, 1, 7, 2]

newList4 = list(map(lambda x:x*x, list5))
newList5 = list(filter(lambda x:x>5, list5))

print(f"The Squared list is: {newList4}")
print(f"The List is(Each Item > 4): {newList5}")


# Reduce Function: Groups up every elements in what way need
from functools import reduce

list9 = [3, 4, 6, 8]

newList9 = reduce(lambda x, y: x + y, list9)
print(f"The sum of numbers of the list: {newList9}")