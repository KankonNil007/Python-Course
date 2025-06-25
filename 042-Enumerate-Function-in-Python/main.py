# Enumerate Function in Python

# Simple For Loop

marks = [12, 34, 56, 24, 78, 89, 98, 45, 77]
index = 0

for mark in marks:
    print(mark)
    if (index == 6):
        print("Kankon, well done!")

    index = index + 1

print("\n\n")
# The Same Loop using Enumerate Function

marks2 = [12, 34, 56, 89, 98, 45, 77]

for index, mark in enumerate(marks2):
    print(mark)

    if (index == 4):
        print("Kankon Awesome!!!")

print("\n\n")
# Start Attribute in Enumerate Function

marks3 = [34, 56, 89, 98, 45, 77]

for index, mark in enumerate(marks3, start=1):
    print(mark)

    if (index == 4):
        print("Kankon Awesome!!!")

# Looping over a String

s = 'hello'
for index, c in enumerate(s):
    print(index + 1, c)