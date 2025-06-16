# List Methods in Python

# Sort Method

list1 = [12, 2, 6, 23, 17, 7]
print(list1)

list1.sort() # Sorts the list small to big
print(list1)

list1.sort(reverse=True) # Sorts the list big to small
print(list1)

# Reverse Method

list2 = [4, 6, 76, 34, 12, 44]
print(list2)

list2.reverse() # Turns the list into opposite list
print(list2)

# Index Method

list3 = [2, 3, 1, 4, 4, 6, 3, 2, 4]
print(list3)

print(list3.index(2)) # it gives the index of the first occurence of a value in a list
print(list3.index(3))
print(list3.index(4))
print(list3.index(1))

# Count Method

list3 = [2, 3, 1, 4, 4, 6, 3, 2, 4]
print(list3)

print(list3.count(4)) # How many times this value occured in a list
print(list3.count(2))
print(list3.count(1))

# Copy Method

# A Mistake that everyone does in Python
list5 = ["Apple", "Banana", "Berry", "Coconut"]
list6 = list5
list6[2] = "Strawberry"
print(list5) # This doesn't print the original one

# The Solution is the Copy method

list5 = ["Apple", "Banana", "Berry", "Coconut"]
list6 = list5.copy()
list6[2] = "Strawberry"
print(list5)

# Append Method

list7 = [2, 4, 6, 3]
print(list7)

list7.append(7) # This adds 7 to the list as a new (last) item
print(list7)

# Insert Method

list8 = [2, 4, 6, 3]
print(list8)

list8.insert(2, 45) # This adds 45 to the list in the 2nd index
print(list8)

# Extend Method

list9 = [2, 4, 5]
list10 = [6, 3, 1]

list9.extend(list10) # This adds list10 to list9
print(list9)

# Concatenating Lists

list11 = [2, 4, 5]
list12 = [6, 3, 1]
list13 = [16, 33, 14]

list99 = list11 + list12 + list13
print(list99)