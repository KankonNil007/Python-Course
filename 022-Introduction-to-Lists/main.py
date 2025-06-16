# Lists in Python

# Example of a List
marks = [70, 75, 80]
print(marks)
print(type(marks))

# We can also select a certain value of a list

print(marks[0])
print(marks[1])
print(marks[2])

# We can also store multiple types of data in a single list

multiData = ["Kankon", 7, True]
print(multiData)

# Negative Indexing

marks2 = [70, 75, 78, 80, 87, 94]
print(marks2[-4]) # print(marks2[len(marks2)-4]) = 2

# If-Else Condition in Lists

marks2 = [70, 75, 78, 80, 87, 94]

if 87 in marks2:
    print("87 is in the list")
else:
    print("87 is not in the list")

# Same condition applies for a String

if "Kan" in "Kankon":
    print("Yes")
else:
    print("No")

# List Ranging

# Syntax : listname[start : end : jumpindex]

marks3 = [12, 24, 33, 35, 46, 53, 48, 67, 80, 99, 23]

print(marks3[:]) # Auto completes with 0 and len(marks3)
print(marks3[1:10])
print(marks3[1:10:2])
print(marks3[1:10:3])

# List Comprehension (Complex Lists)

num1 = [i for i in range(5)]
print(num1)

num2 = [i*i for i in range(10)]
print(num2)

num3 = [i*i for i in range(10) if i%2 == 0]
print(num3)

num4 = [(2*i+1) for i in range(10) if i%2 == 0]
print(num4)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)