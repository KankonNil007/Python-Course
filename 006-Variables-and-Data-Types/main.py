# Variables and Data Types

# Number Data Type
var1 = 43
print(var1)

# String Data Type
var2 = "Kankon"
print(var2)

# Boolean Data Type
var3 = True
print(var3)

# Undefined/Null Data Type
var4 = None
print(var4)

# You can also overwrite a variable
# Although it will before overwriting it, it will show the previous value
var0 = 45
print(var0)
var0 = 23
print(var0)

# BODMAS Rule
var5 = 23
print(var1 + var5)

# We can check what type of variable it is
print(type(var1))
print("This variable is ", type(var2))
print("This variable is ", type(var3))
print("This variable is ", type(var4))

# There are Three types of numbers :
# Integer, Float, Complex

num1 = 23
num2 = 34.54
num3 = complex(8, 4)

print(num1, num2, num3)

# List and Tuples
# Tuples are special kind of list that can't be changed

list1 = [8, 2.3, ["apple", "banana"], [2, 3]]
tuple1 = (("parrot", "sparrow"), ("Kankon", "Nil"))

print(list1, tuple1)

# Mapped / Dictionary Data Type
dict1 = {"Name": "Kankon", "Age": 20, "CanVote": True}
print(dict1)

# Casting - You can define the variable what type of variable it is

cast1 = str(5) # cast1 = "5"
cast2 = int(5) # cast2 = 5
cast3 = float(5) # cast3 = 5.0

# Assigning Multiple Values to Variables
x, y, z = "apple", "banana", "mango"
print(x)
print(y)
print(z)

# How to unpack a Collection or List

fruit3 = ["apple", "banana", "mango"]
x1, y1, z1 = fruit3
print(x1)
print(y1)
print(z1)

# Global Variable
global var100
var100 = 23
# var100 is declared as global variable. So, whenever it is used in function, loop, statements, it will not show any error.