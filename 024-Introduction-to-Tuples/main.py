# Introduction to Tuples in Python

# Example of a Tuple 

tuple1 = (1, 5, 9)
print(tuple1)
print(type(tuple1))

# Problem of a Tuple

tuple2 = (1) # This will print as a int variable
print(type(tuple2))

# So we have to use a comma in the value of a tuple if a tuple has a single value

tuple2 = (1,)
print(type(tuple2))

# We can also use tuple with multiple data types like lists

tuple3 = ("Kankon", 9, True)
print(tuple3)

# The only difference between lists and tuples is list's value can be changed and tuple's value can't be. 

# You can also print certain values of a tuple like list

tuple4 = (9, 5, 3, 6, 2)
print(tuple4[2])
print(tuple4[1])
print(tuple4[3])
print(tuple4[0])

# Negative Index can be added

print(tuple4[-3])
print(tuple4[-1])

# If-Else Condition in Tuple

tuple4 = (9, 5, 3, 6, 2)

if 5 in tuple4:
    print("Yes, 5 is Present")
else:
    print("No, 5 is not Present")

# Tuple Ranging

# Syntax : tuplename[start : end : jumpindex]

tuple5 = (12, 24, 33, 35, 46, 53, 48, 67, 80, 99, 23)

print(tuple5[:]) # Auto completes with 0 and len(tuple5)
print(tuple5[1:10])
print(tuple5[1:10:2])
print(tuple5[1:10:3])