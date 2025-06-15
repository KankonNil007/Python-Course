# Sum of Digits of a Number in Loops

# Input a number and print the sum of its digits.

inputNum = int(input("Enter a Number: "))
orgNum = inputNum
totalSum = 0

while inputNum > 0:
    digit = inputNum % 10
    totalSum = totalSum + digit
    inputNum = inputNum // 10

print("The Sum of", orgNum,"digits is", totalSum)