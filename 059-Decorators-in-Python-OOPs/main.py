# Decorators in Python(OOPs)

def greet(fx): # defining a decorator
    def mfx():
        print("Hello Guys. Good Morning!")
        fx()
        print("Thanks for using this")
    return mfx

@greet # Decorator Usage
def hello():
    print("Hello World!!!!!")

# greet(hello)()
hello()

# args and kwargs parameter

def greet(fx): # defining a decorator
    def mfx(*args, **kwargs):
        print("Hello Guys. Good Morning!")
        fx(*args, **kwargs)
        print("Thanks for using this")
    return mfx

@greet
def add(a, b):
    print(f"The sum of {a} and {b} is: {a+b}")

# greet(add)(1, 5)
add(1, 5)