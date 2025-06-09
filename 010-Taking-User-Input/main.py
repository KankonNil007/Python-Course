# Taking User Input

a = input("Enter your name :")
print("Your name is", a)

# One of the Input Problems

x = input("Enter First Number : ")
y = input("Enter Second Number : ")

# print(x + y)
# Answer is in String Format so it is wrong
# Example: 45 + 34 = 4534 , it thinks the numbers as a string

print("The Summation of the numbers is",int(x) + int(y)) # Solution

# Typecasting in Input Functions

inp1 = float(input("Input any float number: "))
inp2 = int(input("Input any Integer number: "))

print("The multiplication of the numbers is :", inp1 * inp2)