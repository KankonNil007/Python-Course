# Simple Calculator Using If-Else Statements

print("SIMPLE CALCULATOR")

num1 = float(input("Enter your first Number: "))

operator = input("Enter any Operation(+, -, *, /): ")

num2 = float(input("Enter your second Number: "))

if ("+" == operator):
    print("The result of", num1, operator, num2,"=", num1 + num2)
elif ("-" == operator):
    print("The result of", num1, operator, num2,"=", num1 - num2)
elif ("*" == operator):
    print("The result of", num1, operator, num2,"=", num1 * num2)
elif ("/" == operator and num2 == 0):
    print("You can't Divide by Zero")
elif ("/" == operator):
    print("The result of", num1, operator, num2,"=", num1 / num2)
else:
    print("Invalid Input")