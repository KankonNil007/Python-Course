# Lambda Functions in Python

# Lambda Functions are a shorthand Function which are used instead of small functions

# def double(x):
#     return x*2

# We can instead use lambda function in this regard

double = lambda x : x * 2
cube = lambda x : x * x * x

print(f"The double of 5 is: {double(5)}")
print(f"The cube of 5 is: {cube(5)}")

# This can use multiple values too

avg = lambda x,y,z : (x+y+z)/3

print(f"The average of 34, 76 and 83 is: {avg(34, 76, 83)}")


# These small functions can be used inside a function or something like nested function

cube = lambda x : x * x * x

def apple(a, b):
    return 50 + a(b)

print(f"The sum of 50 and 5 cube is: {apple(cube, 5)}")