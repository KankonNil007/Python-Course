# Local and Global Variables in Python

x = 4 # Global Variable - Can be used anywhere

def hello():
    x = 5 # Local Variable - Can't be used outside this function
    print(f"The local value of x is: {x}")

hello()

print(f"The global value of x is: {x}")


# How to change a global variable inside a function

x = 10

def hello2():
    global x # This will overwrite the value of x which is a global variable
    x = 4
    print(x)

hello2()
print(x)