# Operations on Tuples in Python

# You can't directly change a tuple. You have to convert it to a list , thrn make some changes and then change it back to tuple. 

countries = ("Bangladesh", "India", "Pakistan", "Sri Lanka", "Afghanistan")
print(countries)

countriesList = list(countries)
countriesList.append("Nepal") # add item
countriesList.pop(2) # remove item
countriesList[3] = "Bhutan" # change item
countries = tuple(countriesList)

print(countries)

# Concatenating Tuples

tuple1 = (2, 4, 6)
tuple2 = (1, 3, 5)

tuple3 = tuple1 + tuple2

print(tuple3)

# Count Method in Tuples : counts the occurence number of a certain value

tuple4 = (1, 1, 3, 5, 7, 3, 2, 4, 1, 3, 5, 6)
print("The count of 3 is", tuple4.count(3))

# Index Method : Tells us the indexing number of a certain value

tuple5 = (1, 1, 3, 5, 7, 3, 2, 4, 1, 3, 5, 6, 6)
print("The index of 4 is", tuple4.index(4))

# Advanced Indexing

# Syntax : index(value, start, stop)

tuple6 = (1, 1, 3, 5, 7, 3, 2, 4, 1, 3, 5, 6, 6)
print("The index of 3 in 4:8 is", tuple4.index(3, 4, 8))

# Tuple Length

tuple7 = (1, 1, 3, 5, 7, 3, 2, 4, 1)
print("The length of tuple7 is", len(tuple7))