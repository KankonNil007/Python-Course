# Multiplication Table Using Loops

# Ask the user for a number and print its multiplication table up to 10.

inputNum = int(input("Enter a number: "))

for i in range(1, 11):
    print(inputNum, "x", i,"=", inputNum * i)