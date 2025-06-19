# Recursive Factorial & Fibonacci Generator

# Topics used: recursion, f-strings

# Factorial Generator

num = int(input("Enter a Number: "))

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)
    
print(f"The Factorial of {num} is: {factorial(num)}")

# Fibonacci Generator

num2 = int(input("Enter the Position of the Fibonacci Number: "))

def fibonacci(num2):
    if (num2 == 1):
        return 0
    elif (num2 == 2):
        return 1
    
    fibolist = [0, 1]

    for i in range(2, num2 + 1):
        fibolist.append(fibolist[i -1] + fibolist[i -2])

    return fibolist[num2]

print(f"The {num2}th Fibonacci Number is: {fibonacci(num2)}")