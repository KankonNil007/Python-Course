# Division Calculator with Final Message
    
# Concepts: try-except-finally, raise

# 📝 Task:

# Take two numbers as input and divide them.

# Catch division by zero using try-except.

# Raise a ValueError if input is not a number.

# Use finally to say: "Thanks for using the calculator!".

try:
    inpNum1 = int(input("Enter 1st Number: "))
    inpNum2 = int(input("Enter 2nd Number: "))
    
    if (inpNum2 == 0):
        raise ZeroDivisionError("Can't Divide by Zero")
    else:
        print(f"Division Result: {inpNum1 / inpNum2}")
except ValueError:
    print("Not a Number!!!!")
finally:
    print("Thanks for using the calculator!")