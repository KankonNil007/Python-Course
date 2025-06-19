# Custom Calculator using fStrings in Python

# Topics used: f-strings, docstrings

# Task:
# Create a calculator that supports addition, subtraction, multiplication, and division.
# Use docstrings for each function and display output using f-strings.

num1 = int(input("Enter first Number: "))
symbol = input("Enter (+, -, *, /): ")
num2 = int(input("Enter second Number: "))

def add():
    """
    This function will be used as addition function.
    """
    print(f"The result of {num1} {symbol} {num2} is:{num1 + num2}")

def sub():
    """
    This function will be used as substraction function.
    """
    print(f"The result of {num1} {symbol} {num2} is:{num1 - num2}")

def mul():
    """
    This function will be used as multiplication function.
    """
    print(f"The result of {num1} {symbol} {num2} is:{num1 * num2}")

def div():
    """
    This function will be used as division function.
    """
    print(f"The result of {num1} {symbol} {num2} is:{num1 / num2}")

def calculation():
    """
    This is the main function of the project.
    """

    if (symbol == "+"):
        add()
    elif (symbol == "-"):
        sub()
    elif (symbol == "*"):
        mul()
    elif (symbol == "/"):
        div()
    else:
        print("Invalid Characters!!!")

calculation()