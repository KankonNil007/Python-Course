# Function Arguments in Python

# Average Function
def average(a=5, b=2):
    averNum = (a+b)/2
    print("The average of", a,"and", b,"is", averNum)

average() # Function will consider default value
average(6, 5) # Function will overwrite the default values
average(b=5) # Only changes the b value
average(b=6, a=34) # Changes the order of values

# Another type of Function

def average2(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    average = sum/ len(numbers)
    print("Average is", average)

average2(4, 5, 9)

# Return Statement in Functions

def average2(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    average = sum/ len(numbers)
    return average

c = average2(4, 5, 9, 8)
print(c)

# Dict Functions

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "", lname = "Mondal", fname = "Kankon")