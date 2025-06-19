# Raising Custom Errors in Python

a = int(input("Enter a number between 10 and 15: "))

if (a < 10 or a > 15):
    raise ValueError("The number should be between 10 and 15")

print(f"The number you inputed is: {a}")