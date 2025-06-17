# Even or Odd Number List

# Topics: Lists, Functions, If-Else

# What it does:
# Ask the user for 5 numbers. Tell how many are even and how many are odd.


num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
num4 = int(input("Enter Number 4: "))
num5 = int(input("Enter Number 5: "))

numlist = []
oddList = []
evenList = []

numlist.append(num1)
numlist.append(num2)
numlist.append(num3)
numlist.append(num4)
numlist.append(num5)

def evenOddSepareter():
    for i in numlist:
        if (i % 2 == 0):
            evenList.append(i)
        elif (i % 2 != 0):
            oddList.append(i)
        else:
            print("Not a Valid number")

    print("\nEven:", evenList)
    print("Odd:", oddList)

evenOddSepareter()