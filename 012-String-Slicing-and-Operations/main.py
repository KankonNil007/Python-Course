# String Slicing and Operations

names = "Kankon,Sagor"

print(names[0:6]) # Slicing
print(len(names)) # Denotes the length of a string

fruit = "Mango"
print(fruit, "is a", len(fruit),"letter word")

# More about String Slicing

fruit2 = "Apple"

print(fruit2[0:5])
print(fruit2[1:5])
print(fruit2[:5])

"""If you add any negative number in the range, it will automatically add the length of the string and subtract the negative number"""

print(fruit2[0:-2])
# print(fruit2[0:len(fruit2)-2]) 0:3

print(fruit2[-1:-3]) # Doesn't make sense 4:2

print(fruit2[-3:-1]) # Makes sense 2:4

# Looping through a String

alphabets = "ABCDE"
for i in alphabets:
    print(i)

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])
# Ans: This will print out ar