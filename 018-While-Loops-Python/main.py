# While and Do while Loops in Python

# While Loops:

i = 1
while (i <= 3):
    print(i)
    i = i + 1

# We use for loops for simple functions and while loops for complex functions. 

i = 0
while (i <= 50):
    i = int(input("Enter your Number: "))
    print(i)

print("Finally, you have inputed something over than 50\nThe Loop is now over.")

# Decrementing While Loop

i = 5
while (i > 0):
    print(i)
    i = i - 1

print("\n\n")

# Else in While Loops

i = 5
while (i > 0):
    print(i)
    i = i - 1
else:
    print("The Loop is Over")

"""

There are no specific structures for do while loops
in Python. So, We have to implement it using While
Loops.

Do While Loops are such kinds of loops which runs 
the loop body first time and then checks the condition
 if it's true, then runs the loop body and continues.

"""

# Example:

i = int(input("Enter your Number: "))
print(i)
while (i <= 50):
    i = int(input("Enter your Number: "))
    print(i)

print("Finally, you have inputed something over than 50\nThe Loop is now over.")