"""

Ask the user to input two numbers and an operation (+, -, *, /). Use match-case to perform the correct operation.

"""

# The Result should be like this:

"""

Enter first number: 5  
Enter second number: 2  
Enter operation (+, -, *, /): *  
Output: 10

"""

# Let's Start the project

firstNum = int(input("Enter First Number:"))

secondNum = int(input("Enter Second Number:"))

operation = input("Enter Operation (+, -, *, /):")

match operation:
    case "+":
        print("Output:", firstNum + secondNum)
    case "-":
        print("Output:", firstNum - secondNum)
    case "*":
        print("Output:", firstNum * secondNum)
    case "/":
        print("Output:", firstNum / secondNum)