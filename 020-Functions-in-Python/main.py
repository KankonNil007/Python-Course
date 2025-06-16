# Functions in Python

# Geometric Mean Calculating Function
def calcGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

# Number Checker Function
def numbChecker(a, b):
    if(a > b):
        print("a is the bigger Number.")
    elif(b > a):
        print("b is the bigger Number")
    else:
        print("a and b are equal")

# If you wanna write a function later but define it now
def numbChecker2(a, b):
    pass

a = 9
b = 6
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calcGmean(a, b)
numbChecker(a, b)

c = 14
d = 23
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calcGmean(c, d)
numbChecker(c, d)